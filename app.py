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

DIS_REGEX = re.compile('^(dis)_[^ ]+_\\1$')
QUERY = ""

def txt_to_doc(txt):
    splitted = txt.split()
    # return (docid, words)
    return splitted[0], [w for w in splitted[1:] if DIS_REGEX.match(w) or w == QUERY]

def doc_to_words(doc):
    words = doc[1]
    num_words = len(words)
    ret = []
    for word in words:
        ret.append(((doc[0], num_words, word), 1))
    return ret

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Invalid number of arguments, program expects only filename '
              'relative to `data` directory to analyze and query term.')
        exit(0)

    filename = sys.argv[1]

    QUERY = sys.argv[2]
    output = open('output', 'w')

    output.write(f'Query: {QUERY}\n')

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
    tf_idf_merged = tf_idf.map(lambda word: (word[0], {i[0]: word[1][0] * i[1] for i in word[1][1]}))
    # DEBUG: tf_idf_merged.saveAsTextFile('tf_idf')

    sorted_tf_idf = tf_idf_merged.sortByKey()
    q = sorted_tf_idf.lookup(QUERY)
    q = [i for i in q]
    q_norm = sum(map(lambda x: x ** 2, q[0].values())) ** (1/2)

    similartities = tf_idf_merged.map(lambda w: (w[0], sum([q[0][elem] * w[1][elem] for elem in q[0].keys() & w[1].keys()]) / (sum(map(lambda x: x ** 2, w[1].values())) ** (1/2) * q_norm)))

    sorted_similartities = similartities.sortBy(lambda word: word[1], False)
    terms = sorted_similartities.take(6)

    output.write(f'\nTop 5 similar to {QUERY}:\n')
    # query should match itself, so we skip that
    output.writelines([f'{word} {item}\n' for (word, item) in terms[1:]])
    output.close()
