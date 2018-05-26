import sys,string,random,time

PREFIX = sys.argv[1:]


ancestral = {}
for P in PREFIX:
    extant_genes = {}
    ancestral[P] = {}
    file_genes = open(P+".genes.txt","r").readlines()
    for line in file_genes:
        words = line.split()
        species = words[0]
        ident = words[1]
        if len(words) == 2:
            if not extant_genes.has_key(species):
                extant_genes[species] = 0
            extant_genes[species] = extant_genes[species] + 1
        else:
            if not ancestral[P].has_key(species):
                ancestral[P][species] = 0
            ancestral[P][species] = ancestral[P][species] + 1


ekeys = extant_genes.keys()

output = open("comparison_contents.txt","w")
for i in range(len(ekeys)):
    output.write(str(extant_genes[ekeys[i]])+" ")
    for P in PREFIX:
        keys = ancestral[P].keys()
        if i<len(keys):
            output.write(str(ancestral[P][keys[i]])+" ")
        else:
            output.write("NA ")
    output.write("\n")

    
output = open("comparison_degrees.txt","w")
degree = {}
for P in PREFIX:
    degree[P] = {}
    file_adjacencies = open(P+".adjacencies.txt","r").readlines()
    for line in file_adjacencies:
        words = line.split()
        species = words[0]
        gene1 = words[1]
        gene2 = words[2]
        if len(words) > 6:
            score = float(words[6])
        else:
            score = 1.0
        if line.find("@") < 0:
            if not degree[P].has_key(gene1):
                degree[P][gene1] = 0.0
            if not degree[P].has_key(gene2):
                degree[P][gene2] = 0.0
            degree[P][gene1] = degree[P][gene1] + score
            degree[P][gene2] = degree[P][gene2] + score

max_value = 0
for P in PREFIX:
    max_value = max(max_value,max(degree[P].values()))
nb_categories = int(max_value)
tab = {}
for P in PREFIX:
    tab[P] = [0]*(nb_categories+1)
    for gene in degree[P].keys():
        value = int(nb_categories*degree[P][gene]/max_value)
        tab[P][value] = tab[P][value] + 1
for i in range(nb_categories):
    output.write(str(i*max_value/nb_categories)+" ")
    for P in PREFIX:
        output.write(str(tab[P][i]/float(sum(ancestral[P].values())))+" ")
    if i == 2:
        output.write("1\n")
    else:
        output.write("0\n")







