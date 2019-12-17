ARGS?=data/sample.txt
.PHONY: default init clean

default:
	@python app.py ${ARGS}

init:
	pip install -r requirements.txt

clean:
	rm -rf __pycache__
