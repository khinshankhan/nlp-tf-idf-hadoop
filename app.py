"""
nlp_tf_idf_hadoop.py
NLP analysis of Term Frequency - Inverse Document Frequency using Hadoop
Handles the primary functions
"""

import sys
import pyspark

sc = pyspark.SparkContext('local[*]', 'nlp_tf_idf')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Invalid number of arguments, program expects only filename '
              'relative to `data` directory to analyze.')
        exit(0)

    filename = sys.argv[1]
    output = open('output', 'w')

    txt = sc.textFile(filename)
    output.write(f'Lines in text: {txt.count()}\n')
    words = txt.flatMap(lambda line: line.split())
    output.write(f'Words in text: {words.count()}\n')

    output.close()
