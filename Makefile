ARGS?=data/sample.txt
.PHONY: default init clean

default:
	@python nlp_tf_idf_hadoop ${ARGS}

init:
	pip install -r requirements.txt

clean:
	rm -rf */__pycache__
