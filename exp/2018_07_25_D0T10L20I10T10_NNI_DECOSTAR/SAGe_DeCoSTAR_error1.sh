#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --mem-per-cpu=4G
#SBATCH --account=rrg-chauvec
#SBATCH --output /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_25_D0T10L20I10T10_NNI_DECOSTAR/traces/DeCoSTAR/traces_e1
#SBATCH --error  /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_25_D0T10L20I10T10_NNI_DECOSTAR/traces/DeCoSTAR/errors_e1

echo "Lambda=50"
./run_DeCoSTAR_1.sh /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_25_D0T10L20I10T10_NNI_DECOSTAR/results/NNI/lambda_50 /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_24_NODUP_NNI_DECOSTAR/results/DeCoSTAR_1/ lambda_50

echo "Lambda=50"
./run_DeCoSTAR_2.sh /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_25_D0T10L20I10T10_NNI_DECOSTAR/results/NNI/lambda_50 /home/chauvec/wg-anoph/BOOK_PHYLOGENOMICS/SAGe/exp/2018_07_24_NODUP_NNI_DECOSTAR/results/DeCoSTAR_2/ lambda_50
