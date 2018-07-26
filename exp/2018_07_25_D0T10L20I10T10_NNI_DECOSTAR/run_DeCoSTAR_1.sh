#!/bin/bash

DATA=$1   # Gene trees directory, absolute name
OUTPUT=$2 # Output directory
PREFIX=$3 # Output prefix

PWD=`pwd`
CODE=${PWD}/code
RESULTS=${OUTPUT}/${PREFIX}

ls -d -1 ${DATA}/*nwk > ${PREFIX}_list

sed 's/XXX/'$PREFIX'/g' DeCoSTAR_parameters_1 > ${PREFIX}_DeCoSTAR_parameters_1
${CODE}/DeCoSTAR parameter.file=${PREFIX}_DeCoSTAR_parameters_1
mv ${PREFIX}_DeCoSTAR_parameters_1 ${RESULTS}/
mv ${PREFIX}_list ${RESULTS}/
