

# This script transforms a simulyon output into a decostar input
# Produces the following files:
# - species tree
# - gene tree and gene tree list
# - adjacencies
# - parameters
#
#
# INPUT : 
# - directory of the simulyon output (the input of this script)
# - directory of the decostar input (the output of this script)



import string,sys,math,random,script_tree,os

parameters = sys.argv[1:]
if len(parameters) < 2:
    print "usage: python simulyon_to_decostar.py simulyon_dir decostar_dir"
    exit()

simulyon_dir = parameters[0]
decostar_dir = parameters[1]

parameter_file = open(decostar_dir+"/parameters.txt","w")

species_tree = script_tree.readTree(open(simulyon_dir+"/T/ExtantTree.nwk","r").readline())
root = script_tree.getRoot(species_tree)
all_species = script_tree.getLeavesNames(species_tree)
species_tree_output_file = open(decostar_dir+"/species_tree","w")
species_tree_output_file.write(script_tree.writeTree(species_tree,root,False))
parameter_file.write("species.file=species_tree\n")

gene_trees_files = os.listdir(simulyon_dir+"/G/Gene_trees/")
list_gene_tree = open(decostar_dir+"/list_gene_trees","w")
parameter_file.write("gene.distribution.file=list_gene_trees\n")
chromosomes = open(decostar_dir+"/chromosomes","w")
for s in all_species:
    chromosomes.write(s+" 1\n")
parameter_file.write("chromosome.file=chromosomes\n")

all_genes = {}
for s in all_species:
    all_genes[s] = {}
for file_name in gene_trees_files:
    if string.find(file_name,"pruned") >= 0:
        gene_tree = open(simulyon_dir+"/G/Gene_trees/"+file_name,"r").readline()
        if gene_tree != ":1;":
            gene_tree = script_tree.readTree(gene_tree)
            root = script_tree.getRoot(gene_tree)
            leaves = script_tree.getLeaves(gene_tree,root)
            for l in leaves:
                words = script_tree.getName(gene_tree,l).split("_")
                species = words[0]
                all_genes[species][words[1]] = []
            output = open(decostar_dir+"/gene_trees/"+file_name,"w")
            output.write(script_tree.writeTree(gene_tree,root,False))
            list_gene_tree.write("gene_trees/"+file_name+"\n")


genome_files = os.listdir(simulyon_dir+"/G/Genomes/")
adjacencies = open(decostar_dir+"/adjacencies","w")

for file_name in genome_files:
    species = file_name.split("_")[0]
    if species in all_species:
        file_genome = open(simulyon_dir+"/G/Genomes/"+file_name,"r").readlines()
        i = 1
        while i < len(file_genome):
            line_i = file_genome[i].split()
            if i < len(file_genome) - 1:
                line_i1 = file_genome[i+1].split()
            else:
                line_i1 = file_genome[1].split()
            gene1 = species+"_"+line_i[3]
            dir1 = line_i[2]
            gene2 = species+"_"+line_i1[3]
            dir2 = line_i1[2]
            if not all_genes[species].has_key(line_i[3]) or not all_genes[species].has_key(line_i1[3]):
                print "BUG BUG BUG",gene1,gene2,all_genes[species].keys()
            adjacencies.write(species+" "+gene1+" "+gene2+" "+dir1+" "+dir2+" 1.0\n")
            i = i + 1


#output.dir=results/Xtopo/b_10000_loss.aware
#output.prefix=ADseq_21Anopheles_b10000_loss.aware_Xtopo_Boltz_0.1


#with.transfer=0
#dated.species.tree=0
#char.sep=@
#ale=0
#already.reconciled=0

#verbose=1

#dupli.cost=2
#HGT.cost=3
#loss.cost=1
#try.all.amalgamation=0
#rooted=0

#AGain.cost=3
#ABreak.cost=1
#C1.Advantage=0.5

#Loss.aware=1
#Loss.iteration=2

#scaffolding.mode=1
#adjacency.score.log.base=10000
#scaffolding.propagation.index=21
#scaffold.includes.scored.adjs=false

#use.boltzmann=1
#boltzmann.temperature=0.1
#nb.sample=100

#write.newick=1
#hide.losses.newick=0
#write.adjacencies=1
#write.genes=1
#write.adjacency.trees=0


#all.pair.equivalence.class=0
#bounded.TS=0
#always.AGain=1
#absence.penalty=-1
#substract.reco.to.adj=0
#Topology.weight=1
#Reconciliation.weight=1
#Adjacency.weight=1
#")