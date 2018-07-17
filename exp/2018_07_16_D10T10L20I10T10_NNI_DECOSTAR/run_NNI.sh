#!/bin/bash

LAMBDA=$1 # Esperance of the Poisson law
OUTPUT=$2 # Output directory
DATA=$3   # Gene trees directory, absolute name
PWD=`pwd`
CODE=${PWD}/code
RESULTS=${PWD}/results/NNI/${OUTPUT}

cd ${DATA}
TREES=`ls *nwk`

cd ${CODE}
for T in ${TREES}
do
     TREE=${DATA}/${T}
    echo $TREE
    python random_NNI_poisson.py ${TREE} ${LAMBDA} > ${RESULTS}/${T}
done
cd ${PWD}
