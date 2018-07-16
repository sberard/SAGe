#!/bin/bash

echo "#dataset nb_dup nb_loss rec_score nb_gain nb_break DeCo_score linearity_score" > results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR/lambda_025/ lambda_025 >> results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR/lambda_05/ lambda_05   >> results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR/lambda_1/ lambda_1     >> results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR/lambda_2/ lambda_2     >> results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR/lambda_3/ lambda_3     >> results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR/lambda_5/ lambda_5     >> results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR/lambda_7/ lambda_7     >> results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR/lambda_10/ lambda_10   >> results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR/lambda_20/ lambda_20   >> results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR/lambda_30/ lambda_30   >> results/summary_1
python code/DeCoSTAR_scores.py results/DeCoSTAR/lambda_50/ lambda_50   >> results/summary_1
