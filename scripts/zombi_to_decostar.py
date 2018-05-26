

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
# - name of the instance (to name the parameter file and gene trees directory)



import string,sys,math,random,script_tree,os

parameters = sys.argv[1:]
if len(parameters) < 3:
    print "usage: python simulyon_to_decostar.py simulyon_dir decostar_dir name"
    exit()

simulyon_dir = parameters[0]
decostar_dir = parameters[1]
expname = parameters[2]

parameter_file = open(decostar_dir+"/parameters_"+expname+".txt","w")
directory = decostar_dir+"/gene_trees_"+expname
if not os.path.exists(directory):
    os.mkdir(directory)

#print "read species tree"
species_tree = script_tree.readTree(open(simulyon_dir+"/T/ExtantTree.nwk","r").readline())
root = script_tree.getRoot(species_tree)
all_species = script_tree.getLeavesNames(species_tree)
species_tree_output_file = open(decostar_dir+"/species_tree","w")
species_tree_output_file.write(script_tree.writeTree(species_tree,root,False))
parameter_file.write("species.file=species_tree\n")

#print "read gene trees"
gene_trees_files = os.listdir(simulyon_dir+"/G/Gene_trees/")
list_gene_tree = open(decostar_dir+"/list_gene_trees_"+expname,"w")
parameter_file.write("gene.distribution.file=list_gene_trees_"+expname+"\n")
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
        if gene_tree != ";":
            family_name = file_name.split("_")[0]
            #print family_name
            gene_tree = script_tree.readTree(gene_tree)
            root = script_tree.getRoot(gene_tree)
            leaves = script_tree.getLeaves(gene_tree,root)
            for l in leaves:
                words = script_tree.getName(gene_tree,l).split("_")
                species = words[0]
                gene_name = species + "@" + family_name + "_" + words[1]
                all_genes[species][gene_name] = []
                script_tree.setName(gene_tree,l,gene_name)
            output = open(decostar_dir+"/gene_trees_"+expname+"/"+file_name,"w")
            output.write(script_tree.writeTree(gene_tree,root,False))
            list_gene_tree.write("gene_trees_"+expname+"/"+file_name+"\n")

genome_files = os.listdir(simulyon_dir+"/G/Genomes/")
adjacencies = open(decostar_dir+"/adjacencies_"+expname,"w")
parameter_file.write("adjacencies.file=adjacencies_"+expname+"\n")

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
            family_name1 = line_i[1]
            family_name2 = line_i1[1]
            gene1 = species+"@"+family_name1+"_"+line_i[3]
            dir1 = line_i[2]
            gene2 = species+"@"+family_name2+"_"+line_i1[3]
            dir2 = line_i1[2]
            if not all_genes[species].has_key(gene1) or not all_genes[species].has_key(gene2):
                print "BUG BUG BUG",gene1,gene2,all_genes[species].keys()
            adjacencies.write(gene1+" "+gene2+" "+dir1+" "+dir2+" 1.0\n")
            i = i + 1

parameter_file.write("char.sep=@                            \n")
parameter_file.write("\n")
parameter_file.write("output.dir=results/  \n")
parameter_file.write("output.prefix="+expname+"                \n")
parameter_file.write("\n")
parameter_file.write("verbose=1                             \n")
parameter_file.write("\n")
parameter_file.write("with.transfer=1                       \n")
parameter_file.write("dated.species.tree=0                  \n")
parameter_file.write("ale=0                                 \n")
parameter_file.write("already.reconciled=0                  \n")
parameter_file.write("\n")

parameter_file.write("dupli.cost=2                 \n")
parameter_file.write("HGT.cost=3                 \n")
parameter_file.write("loss.cost=1                 \n")
parameter_file.write("try.all.amalgamation=0                 \n")
parameter_file.write("rooted=0                 \n")
parameter_file.write("\n")
parameter_file.write("AGain.cost=3                 \n")
parameter_file.write("ABreak.cost=1                 \n")
parameter_file.write("C1.Advantage=0.5                 \n")
parameter_file.write("\n")
parameter_file.write("Loss.aware=1                 \n")
parameter_file.write("Loss.iteration=2                 \n")
parameter_file.write("\n")
parameter_file.write("scaffolding.mode=0                 \n")
parameter_file.write("adjacency.score.log.base=10000                 \n")
parameter_file.write("scaffolding.propagation.index=21                 \n")
parameter_file.write("scaffold.includes.scored.adjs=false                 \n")
parameter_file.write("\n")
parameter_file.write("use.boltzmann=0                 \n")
parameter_file.write("boltzmann.temperature=0.1                 \n")
parameter_file.write("nb.sample=1                 \n")
parameter_file.write("\n")
parameter_file.write("write.newick=1                 \n")
parameter_file.write("hide.losses.newick=0                 \n")
parameter_file.write("write.adjacencies=1                 \n")
parameter_file.write("write.genes=1                 \n")
parameter_file.write("write.adjacency.trees=0                 \n")
parameter_file.write("\n")
parameter_file.write("all.pair.equivalence.class=0                 \n")
parameter_file.write("bounded.TS=0                 \n")
parameter_file.write("always.AGain=1                 \n")
parameter_file.write("absence.penalty=-1                 \n")
parameter_file.write("substract.reco.to.adj=0                 \n")
parameter_file.write("Topology.weight=1                 \n")
parameter_file.write("Reconciliation.weight=1                 \n")
parameter_file.write("Adjacency.weight=1                 \n")
