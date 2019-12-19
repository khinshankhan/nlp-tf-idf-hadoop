# nlp-tf-idf-hadoop

NLP analysis of Term Frequency - Inverse Document Frequency using Hadoop

Khan_Rafi: Khinshan Khan and Shakil Rafi

## Requirements

- Apache Spark
- Python 3

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
