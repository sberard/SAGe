
1. ---------------------------------
This directory contains the results of running MrBayes and ALE on the datasets D10T0L20I10T10 and D10T10L20I10T10.

The results of ALE only are provided.

For every dataset, the families with three or less sequences were not considered. 
The subdirectory data/ of each of the two experiments contains three files
- D10TYYL20I10T10-families_all (all families)
- D10TYYL20I10T10-families_kept (processed families)
- D10TYYL20I10T10-families_discarded (discarded families)

MrBayes was ran using the script below, where XX is the family ID:<br/>
  begin mrbayes;<br/>
  set autoclose=yes nowarn=yes;<br/>
  execute XX_pruned.nex;<br/>
  prset brlenspr=unconstrained:exp(10.0);<br/>
  mcmcp ngen=10000000;<br/>
  mcmcp Nchains=1;<br/>
   lset nst=6 rates=invgamma ngammacat=4;<br/>
  prset tratiopr = beta(1, 1);<br/>
  lset nst=6;<br/>
  mcmc;<br/>
  sumt;<br/>
  end;

The aim is to generate 20,000 samples for each run. For each family, we do two runs of MrBayes.

The file data/D10TYYL20I10T10-samples provides for each dataset and each family the number of 
sampled trees for both runs.

ALE was ran using a burnin of 5000 trees.
The results for family XX are in the directory results/XX/.

2. ----------------------------------
The directory 2018_07_09_D10T0L20I10T10_NNI contains the result of applying NNIs to the true trees