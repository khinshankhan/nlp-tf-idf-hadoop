"""
nlp_tf_idf_hadoop.py
NLP analysis of Term Frequency - Inverse Document Frequency using Hadoop
Handles the primary functions
"""

import sys
import pyspark
import math

sc = pyspark.SparkContext('local[*]', 'nlp_tf_idf')

def txt_to_doc(txt):
    splitted = txt.split()
    return splitted[0], splitted[1:]

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
    output = open('output', 'w')

    txt = sc.textFile(filename)
    docs = txt.map(txt_to_doc)

    doc_count = docs.count()
    output.write(f'Document count: {doc_count}\n')

    words_by_doc = docs.flatMap(doc_to_words) \
            .reduceByKey(lambda a, b: a + b) # term count per doc
    tf = words_by_doc.map(lambda word: (word[0][2], [(word[0][0], word[1]/word[0][1])])) \
            .reduceByKey(lambda a, b: a + b)
    tf_idf = tf.map(lambda word: (word[0],
        (math.log(doc_count / len(word[1]), 10), word[1]))) # k: word, v: (idf, [tf])
    tf_idf.saveAsTextFile('tf_idf')

    output.close()
