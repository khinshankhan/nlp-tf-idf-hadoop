"""
nlp_tf_idf_hadoop.py
NLP analysis of Term Frequency - Inverse Document Frequency using Hadoop
Handles the primary functions
"""

import sys
import re
import math
import pyspark

sc = pyspark.SparkContext('local[*]', 'nlp_tf_idf')


def txt_to_doc(txt):
    PATTERN1 = re.compile('^dis_.*_dis$')
    PATTERN2 = re.compile('^gene_.*_gene$')
    splitted = txt.split()
    # return (docid, words)
    return splitted[0], [i for i in splitted[1:] if (PATTERN1.match(i) or PATTERN2.match(i))]

def doc_to_words(doc):
    words = doc[1]
    num_words = len(words)
    ret = []
    for word in words:
        ret.append(((doc[0], num_words, word), 1))
    return ret

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Invalid number of arguments, program expects only filename '
              'relative to `data` directory to analyze.')
        exit(0)

    filename = sys.argv[1]
    QUERY = "gene_egfr+_gene"
    output = open('output', 'w')

    txt = sc.textFile(filename)
    docs = txt.map(txt_to_doc)

    doc_count = docs.count()
    output.write(f'Document count: {doc_count}\n')

    words_by_doc = docs.flatMap(doc_to_words) \
            .reduceByKey(lambda a, b: a + b) # term count per doc
    tf = words_by_doc.map(lambda word: (word[0][2], [(word[0][0], word[1]/word[0][1])])) \
            .reduceByKey(lambda a, b: a + b)

    # k: word, v: (idf, [(docid, tf)])
    tf_idf = tf.map(lambda word: (word[0],
        (math.log(doc_count / len(word[1]), 10), word[1])))

    # k: word, v: [(docid, tf*idf)]
    tf_idf_merged = tf_idf.map(lambda word: (word[0], [(i[0], word[1][0] * i[1]) for i in word[1][1]]))
    tf_idf_merged.saveAsTextFile('tf_idf')

    sorted_tf_idf = tf_idf_merged.sortByKey()
    q_term = sorted_tf_idf.lookup(QUERY)[0]
    # DEBUG: print("HERE", q_term)

    output.close()
