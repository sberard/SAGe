#!/bin/bash

echo "#dataset RF nb_dup nb_loss nb_hgt rec_score nb_gain nb_break DeCo_score linearity_score" > results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR_1/lambda_025/ lambda_025 data/list_gene_trees data/gene_trees results/NNI/lambda_025 _1 >> results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR_1/lambda_05/ lambda_05 data/list_gene_trees data/gene_trees results/NNI/lambda_05 _1 >> results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR_1/lambda_1/ lambda_1   data/list_gene_trees data/gene_trees results/NNI/lambda_1  _1 >> results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR_1/lambda_2/ lambda_2   data/list_gene_trees data/gene_trees results/NNI/lambda_2  _1 >> results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR_1/lambda_3/ lambda_3   data/list_gene_trees data/gene_trees results/NNI/lambda_3  _1 >> results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR_1/lambda_5/ lambda_5   data/list_gene_trees data/gene_trees results/NNI/lambda_5  _1 >> results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR_1/lambda_7/ lambda_7   data/list_gene_trees data/gene_trees results/NNI/lambda_7  _1 >> results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR_1/lambda_10/ lambda_10 data/list_gene_trees data/gene_trees results/NNI/lambda_10 _1 >> results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR_1/lambda_20/ lambda_20 data/list_gene_trees data/gene_trees results/NNI/lambda_20 _1 >> results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR_1/lambda_30/ lambda_30 data/list_gene_trees data/gene_trees results/NNI/lambda_30 _1 >> results/summary_1
#python code/DeCoSTAR_scores.py results/DeCoSTAR_1/lambda_50/ lambda_50 data/list_gene_trees data/gene_trees results/NNI/lambda_50 _1 >> results/summary_1

echo "#dataset RF nb_dup nb_loss nb_hgt rec_score nb_gain nb_break DeCo_score linearity_score" > results/summary_2
python code/DeCoSTAR_scores.py results/DeCoSTAR_2/lambda_025/ lambda_025 data/list_gene_trees data/gene_trees results/NNI/lambda_025 _2 >> results/summary_2
python code/DeCoSTAR_scores.py results/DeCoSTAR_2/lambda_05/ lambda_05 data/list_gene_trees data/gene_trees results/NNI/lambda_05 _2 >> results/summary_2
python code/DeCoSTAR_scores.py results/DeCoSTAR_2/lambda_1/ lambda_1   data/list_gene_trees data/gene_trees results/NNI/lambda_1  _2 >> results/summary_2
python code/DeCoSTAR_scores.py results/DeCoSTAR_2/lambda_2/ lambda_2   data/list_gene_trees data/gene_trees results/NNI/lambda_2  _2 >> results/summary_2
python code/DeCoSTAR_scores.py results/DeCoSTAR_2/lambda_3/ lambda_3   data/list_gene_trees data/gene_trees results/NNI/lambda_3  _2 >> results/summary_2
python code/DeCoSTAR_scores.py results/DeCoSTAR_2/lambda_5/ lambda_5   data/list_gene_trees data/gene_trees results/NNI/lambda_5  _2 >> results/summary_2
python code/DeCoSTAR_scores.py results/DeCoSTAR_2/lambda_7/ lambda_7   data/list_gene_trees data/gene_trees results/NNI/lambda_7  _2 >> results/summary_2
python code/DeCoSTAR_scores.py results/DeCoSTAR_2/lambda_10/ lambda_10 data/list_gene_trees data/gene_trees results/NNI/lambda_10 _2 >> results/summary_2
python code/DeCoSTAR_scores.py results/DeCoSTAR_2/lambda_20/ lambda_20 data/list_gene_trees data/gene_trees results/NNI/lambda_20 _2 >> results/summary_2
python code/DeCoSTAR_scores.py results/DeCoSTAR_2/lambda_30/ lambda_30 data/list_gene_trees data/gene_trees results/NNI/lambda_30 _2 >> results/summary_2
#python code/DeCoSTAR_scores.py results/DeCoSTAR_2/lambda_50/ lambda_50 data/list_gene_trees data/gene_trees results/NNI/lambda_50 _2 >> results/summary_2
