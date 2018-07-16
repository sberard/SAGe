#!/bin/bash

DATA=$1   # Gene trees directory, absolute name
OUTPUT=$2 # Output directory
PREFIX=$3 # Output prefix

PWD=`pwd`
CODE=${PWD}/code
RESULTS=${PWD}/results/DeCoSTAR/${OUTPUT}

ls -d -1 ${DATA}/*nwk > ${PREFIX}_list

sed 's/XXX/'$PREFIX'/g' DeCoSTAR_parameters > ${PREFIX}_DeCoSTAR_parameters
${CODE}/DeCoSTAR parameter.file=${PREFIX}_DeCoSTAR_parameters
