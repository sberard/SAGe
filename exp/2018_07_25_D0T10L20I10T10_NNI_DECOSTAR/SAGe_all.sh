#!/bin/bash

SAGe_NNI.sh > traces/NNI/trace
SAGe_DeCoSTAR.sh > traces/DeCoSTAR/trace
SAGe_scores.sh
