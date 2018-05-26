import sys,string,random,time

parameters = sys.argv[1:]

PREFIX_RAW = parameters[0]
PREFIX_PNJ = parameters[1]

extant_genes = {}
ancestral_raw = {}
ancestral_pnj = {}

file_genes = open(PREFIX_RAW+".genes.txt","r").readlines()
for line in file_genes:
    words = line.split()
    species = words[0]
    ident = words[1]
    if len(words) == 2:
        if not extant_genes.has_key(species):
            extant_genes[species] = 0
        extant_genes[species] = extant_genes[species] + 1
    else:
        if not ancestral_raw.has_key(species):
            ancestral_raw[species] = 0
        ancestral_raw[species] = ancestral_raw[species] + 1

file_genes = open(PREFIX_PNJ+".genes.txt","r").readlines()
for line in file_genes:
    words = line.split()
    species = words[0]
    ident = words[1]
    if len(words) > 2:
        if not ancestral_pnj.has_key(species):
            ancestral_pnj[species] = 0
        ancestral_pnj[species] = ancestral_pnj[species] + 1

#print len(extant_genes.keys()),len(ancestral_pnj.keys()),len(ancestral_raw.keys())

ekeys = extant_genes.keys()
rkeys = ancestral_raw.keys()
pkeys = ancestral_pnj.keys()

output = open("comparison_contents.txt","w")
for i in range(len(ekeys)):
    output.write(str(extant_genes[ekeys[i]])+" ")
    if i<len(rkeys):
        output.write(str(ancestral_raw[rkeys[i]])+" ")
    else:
        output.write("NA ")
    if i<len(pkeys):
        output.write(str(ancestral_pnj[pkeys[i]])+"\n")
    else:
        output.write("NA\n")
        
#print "extant"
#for s in ekeys:
    #print s,extant_genes[s]
    
#print "raw"
#for s in rkeys:
    #print s,ancestral_raw[s]
 
#print "pnj"
#for s in pkeys:
    #print s,ancestral_pnj[s]
    
output = open("comparison_degrees.txt","w")
degree = {"PNJ":{},"RAW":{}}
file_adjacencies = open(PREFIX_PNJ+".adjacencies.txt","r").readlines()
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
        if not degree["PNJ"].has_key(gene1):
            degree["PNJ"][gene1] = 0.0
        if not degree["PNJ"].has_key(gene2):
            degree["PNJ"][gene2] = 0.0
        degree["PNJ"][gene1] = degree["PNJ"][gene1] + score
        degree["PNJ"][gene2] = degree["PNJ"][gene2] + score
file_adjacencies = open(PREFIX_RAW+".adjacencies.txt","r").readlines()
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
        if not degree["RAW"].has_key(gene1):
            degree["RAW"][gene1] = 0.0
        if not degree["RAW"].has_key(gene2):
            degree["RAW"][gene2] = 0.0
        degree["RAW"][gene1] = degree["RAW"][gene1] + score
        degree["RAW"][gene2] = degree["RAW"][gene2] + score

max_value = int(max(max(degree["PNJ"].values()),max(degree["RAW"].values())))
nb_categories = int(max_value)
tab = {"PNJ":[0]*(nb_categories+1),"RAW":[0]*(nb_categories+1)}
for gene in degree["RAW"].keys():
    value = int(nb_categories*degree["RAW"][gene]/max_value)
    #print value
    tab["RAW"][value] = tab["RAW"][value] + 1
for gene in degree["PNJ"].keys():
    value = int(nb_categories*degree["PNJ"][gene]/max_value)
    #print degree["PNJ"][gene],value
    tab["PNJ"][value] = tab["PNJ"][value] + 1
for i in range(nb_categories):
    if i == 2:
        output.write(str(i*max_value/nb_categories)+" "+str(tab["RAW"][i]/float(sum(ancestral_raw.values())))+" "+str(tab["PNJ"][i]/float(sum(ancestral_pnj.values())))+" 1\n")
    else:
        output.write(str(i*max_value/nb_categories)+" "+str(tab["RAW"][i]/float(sum(ancestral_raw.values())))+" "+str(tab["PNJ"][i]/float(sum(ancestral_pnj.values())))+" 0\n")







