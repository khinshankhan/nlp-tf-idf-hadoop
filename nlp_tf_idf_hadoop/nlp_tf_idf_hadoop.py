"""
nlp_tf_idf_hadoop.py
NLP analysis of Term Frequency - Inverse Document Frequency using Hadoop
Handles the primary functions
"""

import pyspark
sc = pyspark.SparkContext('local', 'nlp_tf_idf')

def main(filename):
    print(f'Reading from file: {filename}')
    txt = sc.textFile(filename)
    print(f'Lines in text: {txt.count()}')
    words = txt.flatMap(lambda line: line.split())
    print(f'Words in text: {words.count()}')
