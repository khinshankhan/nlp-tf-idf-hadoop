.PHONY: default init clean

default:
	@echo "Running spark-submit..."
ifdef ARGS
	@spark-submit app.py ${ARGS} &> /dev/null
else
	@spark-submit app.py data/sample.txt gene_egfr+_gene &> /dev/null
endif
	@echo "OUTPUT:"
	@cat output

clean:
	rm -rf __pycache__ output
