# nlp-tf-idf-hadoop

NLP analysis of Term Frequency - Inverse Document Frequency using Hadoop

Khan_Rafi: Khinshan Khan and Shakil Rafi

## Requirements

- Apache Spark
  - have `pyspark` on path
- Python 3
  - Note 3.8 and above do not work well with spark
- Python Packages properly in environment:
  - math
  - re
  - sys
## Run

One can run the project two ways:

- Traditional Way

```bash
spark-submit app.py <file_to_parse> <query_term>
cat output
```

- Abstracted Way

```bash
make FILE=<file_to_parse> QUERY=<query_term>
```

## Notes
- Running the program will write relevant output to `output` rather than stdout
