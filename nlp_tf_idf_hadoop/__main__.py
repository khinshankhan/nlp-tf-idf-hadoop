import sys
from nlp_tf_idf_hadoop import main

if __name__ == '__main__':
    # if len(sys.argv)
    if len(sys.argv) != 2:
        print('Invalid number of arguments, program expects only filename '
              'relative to `data` directory to analyze.')
    else:
        main(sys.argv[1])
