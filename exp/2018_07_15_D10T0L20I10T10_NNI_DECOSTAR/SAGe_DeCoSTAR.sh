#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --account=rrg-chauvec
#SBATCH --output /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_15_D10T0L20I10T10_NNI_DECOSTAR/traces/DeCoSTAR/traces
#SBATCH --error  /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_15_D10T0L20I10T10_NNI_DECOSTAR/traces/DeCoSTAR/errors

echo "Lambda=0.25"
mkdir -p results/DeCoSTAR/lambda_025
./run_DeCoSTAR.sh /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_15_D10T0L20I10T10_NNI_DECOSTAR/results/NNI/lambda_025 /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_15_D10T0L20I10T10_NNI_DECOSTAR/results/DeCoSTAR/ lambda_025

echo "Lambda=0.5"
mkdir -p results/DeCoSTAR/lambda_05
./run_DeCoSTAR.sh /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_15_D10T0L20I10T10_NNI_DECOSTAR/results/NNI/lambda_05 /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_15_D10T0L20I10T10_NNI_DECOSTAR/results/DeCoSTAR/ lambda_05

echo "Lambda=1"
mkdir -p results/DeCoSTAR/lambda_1
./run_DeCoSTAR.sh /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_15_D10T0L20I10T10_NNI_DECOSTAR/results/NNI/lambda_1 /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_15_D10T0L20I10T10_NNI_DECOSTAR/results/DeCoSTAR/ lambda_1

echo "Lambda=2"
mkdir -p results/DeCoSTAR/lambda_2
./run_DeCoSTAR.sh /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_15_D10T0L20I10T10_NNI_DECOSTAR/results/NNI/lambda_2 /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_15_D10T0L20I10T10_NNI_DECOSTAR/results/DeCoSTAR/ lambda_2

echo "Lambda=3"
mkdir -p results/DeCoSTAR/lambda_3
./run_DeCoSTAR.sh /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_15_D10T0L20I10T10_NNI_DECOSTAR/results/NNI/lambda_3 /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_15_D10T0L20I10T10_NNI_DECOSTAR/results/DeCoSTAR/ lambda_3

echo "Lambda=5"
mkdir -p results/DeCoSTAR/lambda_5
./run_DeCoSTAR.sh /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_15_D10T0L20I10T10_NNI_DECOSTAR/results/NNI/lambda_5 /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_15_D10T0L20I10T10_NNI_DECOSTAR/results/DeCoSTAR/ lambda_5

echo "Lambda=7"
mkdir -p results/DeCoSTAR/lambda_7
./run_DeCoSTAR.sh /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_15_D10T0L20I10T10_NNI_DECOSTAR/results/NNI/lambda_7 /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_15_D10T0L20I10T10_NNI_DECOSTAR/results/DeCoSTAR/ lambda_7

echo "Lambda=10"
mkdir -p results/DeCoSTAR/lambda_10
./run_DeCoSTAR.sh /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_15_D10T0L20I10T10_NNI_DECOSTAR/results/NNI/lambda_10 /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_15_D10T0L20I10T10_NNI_DECOSTAR/results/DeCoSTAR/ lambda_10

echo "Lambda=20"
mkdir -p results/DeCoSTAR/lambda_20
./run_DeCoSTAR.sh /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_15_D10T0L20I10T10_NNI_DECOSTAR/results/NNI/lambda_20 /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_15_D10T0L20I10T10_NNI_DECOSTAR/results/DeCoSTAR/ lambda_20

echo "Lambda=30"
mkdir -p results/DeCoSTAR/lambda_30
./run_DeCoSTAR.sh /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_15_D10T0L20I10T10_NNI_DECOSTAR/results/NNI/lambda_30 /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_15_D10T0L20I10T10_NNI_DECOSTAR/results/DeCoSTAR/ lambda_30

echo "Lambda=50"
mkdir -p results/DeCoSTAR/lambda_50
./run_DeCoSTAR.sh /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_15_D10T0L20I10T10_NNI_DECOSTAR/results/NNI/lambda_50 /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_15_D10T0L20I10T10_NNI_DECOSTAR/results/DeCoSTAR/ lambda_50
