import sys,string,random,time

def reconciliation_score(rec_file,dup_cost, loss_cost):
    rec_stream = open(rec_file,"r").readlines()
    score=0.0
    for l in rec_stream:
        if l[0]== "(":
            nb_dup  = float(l.count('Dup'))
            nb_loss = float(l.count('Loss'))
            score += nb_dup*dup_cost+nb_loss*loss_cost
    return(score)

def DeCo_score(adjtree_file):
    adjtree_stream = open(adjtree_file,"r").readlines()
    score=0.0
    for l in adjtree_stream:
        if l[0]== ">":
            l1=l.rstrip().replace(': ',':').split()
            for f in l1:
                if f[0:5]=='Score':
                    score+=float(f.split(':')[1])
    return(score)

def linearity_score(gene_file, adj_file):
    # Reading genes list
    genes = {}
    gene_stream = open(gene_file,'r').readlines()
    for l in gene_stream:
        if l[0]!='#':
            l1 = l.rstrip().split()
            species = l1[0]
            ident   = l1[1]
            if not species in genes.keys():
                genes[species] = {}
            genes[species][ident] = []
    # Reading adjacencies list
    adj_stream = open(adj_file,'r').readlines()
    for l in adj_stream:
        if l[0]!='#':
            l1 = l.rstrip().split()
            species = l1[0]
            gene1   = l1[1]
            gene2   = l1[2]
            genes[species][gene1].append(gene2)
            genes[species][gene2].append(gene1)
    # Computing score
    score = 0.0
    for spe in genes.keys():
        for k in genes[spe].keys():
            score += abs(len(genes[spe][k]) - 2)
    return(score)

def extract_rec_costs(param_file):
    param_stream = open(param_file,'r').readlines()
    for l in param_stream:
        if len(l)>1:
            l1=l.rstrip().split('=')
            if l1[0]=='dupli.cost':
                dup_cost = float(l1[1])
            elif l1[0]=='loss.cost':
                loss_cost = float(l1[1])
    return((dup_cost,loss_cost))

## Main

parameters = sys.argv[1:]

if len(parameters) != 2:
    print('usage: python linearity_score.py DIRECTORY PREFIX')
    exit()
    
DIR  = parameters[0]
PREF = parameters[1]

gene_file    = DIR+'/'+PREF+'.genes.txt'
adj_file     = DIR+'/'+PREF+'.adjacencies.txt'
rec_file     = DIR+'/'+PREF+'.reconciliations.newick'
adjtree_file = DIR+'/'+PREF+'.adjacencyTrees.newick'
param_file   = DIR+'/'+PREF+'_DeCoSTAR_parameters'

(dup_cost,loss_cost) = extract_rec_costs(param_file)
rec_score       = reconciliation_score(rec_file,dup_cost, loss_cost)
DeCo_score      = DeCo_score(adjtree_file)
linearity_score = linearity_score(gene_file, adj_file)

print(PREF+'\t'+str(rec_score)+'\t'+str(DeCo_score)+'\t'+str(linearity_score))
