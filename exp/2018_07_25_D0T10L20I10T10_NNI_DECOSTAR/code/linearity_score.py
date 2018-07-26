import sys,string,random,time

parameters = sys.argv[1:]

if len(parameters) != 1:
    print "usage: python linearity_score.py DECOSTAR_PREFIX"
    exit()
    
P = parameters[0]

genes = {}
file_genes = open(P+".genes.txt","r").readlines()
for line in file_genes:
        words = line.split()
        species = words[0]
        ident = words[1]
        if not genes.has_key(species):
            genes[species] = {}
        genes[species][ident] = []


file_adjacencies = open(P+".adjacencies.txt","r").readlines()
for line in file_adjacencies:
        words = line.split()
        species = words[0]
        gene1 = words[1]
        gene2 = words[2]
        genes[species][gene1].append(gene2)
        genes[species][gene2].append(gene1)

score = 0.0
for spe in genes.keys():
    for k in genes[spe].keys():
        score = score + abs(len(genes[spe][k]) - 2)

print score