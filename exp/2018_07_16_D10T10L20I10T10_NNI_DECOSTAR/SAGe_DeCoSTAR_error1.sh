#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --mem-per-cpu=4G
#SBATCH --account=rrg-chauvec
#SBATCH --output /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_16_D10T10L20I10T10_NNI_DECOSTAR/traces/DeCoSTAR/traces_error1
#SBATCH --error  /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_16_D10T10L20I10T10_NNI_DECOSTAR/traces/DeCoSTAR/errors_error1

echo "Lambda=0.25"
mkdir -p results/DeCoSTAR/lambda_025
./run_DeCoSTAR.sh /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_16_D10T10L20I10T10_NNI_DECOSTAR/results/NNI/lambda_025 /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_16_D10T10L20I10T10_NNI_DECOSTAR/results/DeCoSTAR/ lambda_025

