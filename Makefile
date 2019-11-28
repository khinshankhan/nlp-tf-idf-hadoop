.PHONY: default init tests clean

default:
	@python nlp_tf_idf_hadoop ${ARGS}

init:
	pip install -r requirements.txt

tests:
	pytest

clean:
	rm -rf */__pycache__
	rm -rf .pytest_cache
