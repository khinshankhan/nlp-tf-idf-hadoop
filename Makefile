ARGS?=data/sample.txt
.PHONY: default init clean

default:
	@echo "Running spark-submit..."
	@spark-submit app.py ${ARGS} &> /dev/null
	@echo "Output:"
	@cat output

clean:
	rm -rf __pycache__ output
