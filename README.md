# nlp-tf-idf-hadoop
NLP analysis of Term Frequency - Inverse Document Frequency using Hadoop

Khan_Rafi: Khinshan Khan and Shakil Rafi

## Requirements
## Setup
## Run
One can run the project two ways:

- Traditional Way
```bash
python nlp_tf_idf_hadoop <file_to_parse>
```

- Abstracted Way
```bash
make ARGS=<file_to_parse>
```

## Testing
This project uses [pytests](https://docs.pytest.org/en/latest/getting-started.html) testing framework.

- One should install pytests with the command:
```bash
pip install -U pytest
```

- To test all suites:
```bash
pytest
```
or
```bash
make tests
```

## Notes
