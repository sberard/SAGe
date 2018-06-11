This directory contains the results of running MrBayes and ALE on the datasets D10T0L20I10T10 and D10T10L20I10T10.

The results of ALE only are provided.

For every dataset, the families with three or less sequences were not considered. 
The subdirectory data/ of each of the two experiments contains three files
D10TYYL20I10T10-families_all (all families)
D10TYYL20I10T10-families_kept (processed families)
D10TYYL20I10T10-families_discarded (discarded families)

MrBayes was ran using the script below, where XX is the family ID:
  begin mrbayes;
  set autoclose=yes nowarn=yes;
  execute XX_pruned.nex;
  prset brlenspr=unconstrained:exp(10.0);
  mcmcp ngen=10000000;
  mcmcp Nchains=1;
   lset nst=6 rates=invgamma ngammacat=4;
  prset tratiopr = beta(1, 1);
  lset nst=6;
  mcmc;
  sumt;
  end;

The aim is to generate 20,000 samples for each run. For each family, we do two runs of MrBayes.

The file data/D10TYYL20I10T10-samples provides for each dataset and each family the number of 
sampled trees for both runs.

ALE was ran using a burnin of 5000 trees.
The results for family XX are in the directory results/XX/.
