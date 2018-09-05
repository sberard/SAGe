import script_tree,sys

PREFIX = sys.argv[1]

species_tree = script_tree.readTree(open(PREFIX+".speciesTree.newick","r").readline())
genes = open(PREFIX+".genes.txt","r").readlines()
adjacencies = open(PREFIX+".adjacencies.txt","r").readlines()

all_species = {}
root = script_tree.getRoot(species_tree)
nodes = script_tree.getNodes(species_tree)
for n in nodes:
    if script_tree.isLeaf(species_tree,n):
        name = script_tree.getName(species_tree,n).split("@")[0]
        script_tree.setName(species_tree,n,name)
    else:
        name = script_tree.getBootstrap(species_tree,n)
    script_tree.setLength(species_tree,n,1)
    all_species[name] = {}

script_tree.ultrametricize(species_tree)
print script_tree.writeTree(species_tree,root,False)

for line in genes:
    words = line.split()
    if len(words) == 2:
        species = words[1].split("@")[0]
    else:
        species = words[0]
    all_species[species][words[1]] = []

#for n in all_species.keys():
    #print n,len(all_species[n].keys())
    
for line in adjacencies:
    words = line.split()
    gene1 = words[1]
    gene2 = words[2]
    if all_species.has_key(words[0]):
        species = words[0]
    else:
        species = words[1].split("@")[0]
    all_species[species][gene1].append(gene2)
    all_species[species][gene2].append(gene1)

for n in all_species.keys():
    conflict = 0
    for g in all_species[n].keys():
        conflict = conflict + abs(len(all_species[n][g])-2)
    print n,conflict

