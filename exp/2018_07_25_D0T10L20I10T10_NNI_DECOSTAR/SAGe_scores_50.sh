#!/bin/bash

python code/DeCoSTAR_scores.py results/DeCoSTAR_1/lambda_50/ lambda_50 data/list_gene_trees data/gene_trees results/NNI/lambda_50 _1 >> results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR_2/lambda_50/ lambda_50 data/list_gene_trees data/gene_trees results/NNI/lambda_50 _2 >> results/summary_2
