#!/bin/bash

echo "#dataset RF nb_dup nb_loss nb_hgt rec_score nb_gain nb_break DeCo_score linearity_score" > results/summary_1
# 0.25 bugged
#python code/DeCoSTAR_scores.py results/DeCoSTAR/lambda_025/ lambda_025 data/list_gene_trees data/gene_trees results/NNI/lambda_025 >> results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR/lambda_05/ lambda_05 data/list_gene_trees data/gene_trees results/NNI/lambda_05 >> results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR/lambda_1/ lambda_1   data/list_gene_trees data/gene_trees results/NNI/lambda_1  >> results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR/lambda_2/ lambda_2   data/list_gene_trees data/gene_trees results/NNI/lambda_2  >> results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR/lambda_3/ lambda_3   data/list_gene_trees data/gene_trees results/NNI/lambda_3  >> results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR/lambda_5/ lambda_5   data/list_gene_trees data/gene_trees results/NNI/lambda_5  >> results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR/lambda_7/ lambda_7   data/list_gene_trees data/gene_trees results/NNI/lambda_7  >> results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR/lambda_10/ lambda_10 data/list_gene_trees data/gene_trees results/NNI/lambda_10 >> results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR/lambda_20/ lambda_20 data/list_gene_trees data/gene_trees results/NNI/lambda_20 >> results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR/lambda_30/ lambda_30 data/list_gene_trees data/gene_trees results/NNI/lambda_30 >> results/summary_1
#python code/DeCoSTAR_scores.py results/DeCoSTAR/lambda_50/ lambda_50 data/list_gene_trees data/gene_trees results/NNI/lambda_50 >> results/summary_1
