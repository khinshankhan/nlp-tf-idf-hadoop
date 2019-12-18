FILE?="data/sample.txt"
QUERY?="gene_egfr+_gene"
.PHONY: default init clean

default:
	@echo "Running spark-submit..."
	@spark-submit app.py ${FILE} ${QUERY} &> /dev/null
	@echo "OUTPUT:"
	@cat output

clean:
	rm -rf __pycache__ output
