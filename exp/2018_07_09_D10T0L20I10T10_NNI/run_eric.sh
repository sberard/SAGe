#!/bin/bash

LAMBDA=$1 # Esperance of the Poisson law
OUTPUT=$2 # Output directory
DATA=$3

cd ${DATA}
TREES=`ls *nwk`
cd ../code
for T in ${TREES}
do
    TREE=../${DATA}/${T}
    echo $TREE
    python random_NNI_poisson.py ${TREE} ${LAMBDA} > ../results/${OUTPUT}/${T}
done
cd ..
