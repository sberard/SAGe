#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --account=rrg-chauvec
#SBATCH --output /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_16_D10T10L20I10T10_NNI_DECOSTAR/traces/NNI/traces
#SBATCH --error  /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_16_D10T10L20I10T10_NNI_DECOSTAR/traces/NNI/errors

echo "Lambda=0.25"
mkdir -p results/NNI/lambda_025
run_NNI.sh 0.25 lambda_025 /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_16_D10T10L20I10T10_NNI_DECOSTAR/data/gene_trees

echo "Lambda=0.5"
mkdir -p results/NNI/lambda_05
run_NNI.sh 0.5 lambda_05 /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_16_D10T10L20I10T10_NNI_DECOSTAR/data/gene_trees

echo "Lambda=1"
mkdir -p results/NNI/lambda_1
run_NNI.sh 1 lambda_1 /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_16_D10T10L20I10T10_NNI_DECOSTAR/data/gene_trees

echo "Lambda=2"
mkdir -p results/NNI/lambda_2
run_NNI.sh 2 lambda_2 /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_16_D10T10L20I10T10_NNI_DECOSTAR/data/gene_trees

echo "Lambda=3"
mkdir -p results/NNI/lambda_3
run_NNI.sh 3 lambda_3 /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_16_D10T10L20I10T10_NNI_DECOSTAR/data/gene_trees

echo "Lambda=5"
mkdir -p results/NNI/lambda_5
run_NNI.sh 5 lambda_5 /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_16_D10T10L20I10T10_NNI_DECOSTAR/data/gene_trees

echo "Lambda=7"
mkdir -p results/NNI/lambda_7
run_NNI.sh 7 lambda_7 /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_16_D10T10L20I10T10_NNI_DECOSTAR/data/gene_trees

echo "Lambda=10"
mkdir -p results/NNI/lambda_10
run_NNI.sh 10 lambda_10 /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_16_D10T10L20I10T10_NNI_DECOSTAR/data/gene_trees

echo "Lambda=20"
mkdir -p results/NNI/lambda_20
run_NNI.sh 20 lambda_20 /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_16_D10T10L20I10T10_NNI_DECOSTAR/data/gene_trees

echo "Lambda=30"
mkdir -p results/NNI/lambda_30
run_NNI.sh 30 lambda_30 /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_16_D10T10L20I10T10_NNI_DECOSTAR/data/gene_trees

echo "Lambda=50"
mkdir -p results/NNI/lambda_50
run_NNI.sh 50 lambda_50 /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_16_D10T10L20I10T10_NNI_DECOSTAR/data/gene_trees
