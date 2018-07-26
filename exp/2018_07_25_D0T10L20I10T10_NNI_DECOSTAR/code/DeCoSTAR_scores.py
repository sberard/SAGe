import sys,string,random,time,script_tree,numpy

def RF(gene_trees_list,gene_trees_dir1,gene_trees_dir2):# gene_trees_dir1 = true trees, gene_trees_dir2=NNI trees
    ref=open(gene_trees_list,"r").readlines()
    RF=[]
    for line in ref:
        tree_ref = script_tree.readTree(open(gene_trees_dir1+"/"+line.strip(),"r").readline())
        root = script_tree.getRoot(tree_ref)
        tree_comp = script_tree.readTree(open(gene_trees_dir2+"/"+line.strip()).readline())
        RF.append(script_tree.RF(tree_ref,tree_comp))
    return('%.2f' % numpy.mean(RF))


def reconciliation_score(rec_file,dup_cost, loss_cost, hgt_cost):
    rec_stream = open(rec_file,"r").readlines()
    nb_dup=0
    nb_loss=0
    nb_hgt=0
    score=0.0
    for l in rec_stream:
        if l[0]== "(":
            nb_dup  += float(l.count('Dup'))
            nb_loss += float(l.count('Loss'))
            nb_hgt  += float(l.count('Reception'))
    score += nb_dup*dup_cost+nb_loss*loss_cost+nb_hgt*hgt_cost
    return((nb_dup,nb_loss,nb_hgt,score))

def DeCo_score(adjtree_file):
    adjtree_stream = open(adjtree_file,"r").readlines()
    score=0.0
    nb_gain=0
    nb_break=0
    for l in adjtree_stream:
        if l[0]== ">":
            l1=l.rstrip().replace(': ',':').split()
            for f in l1:
                if f[0:5]=='Score':
                    score+=float(f.split(':')[1])
                elif f[0:5]=='#Gain':
                    nb_gain+=int(f.split(':')[1])
                elif f[0:5]=='#Brea':
                    nb_break+=int(f.split(':')[1])                    
    return((nb_gain,nb_break,score))

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
            elif l1[0]=='HGT.cost':
                hgt_cost = float(l1[1])
    return((dup_cost,loss_cost,hgt_cost))

## Main

parameters = sys.argv[1:]

if len(parameters) != 6:
    print('usage: python linearity_score.py DIRECTORY PREFIX TREES_LIST TRUE_TREES_DIR NNI_TREES_DIR SUFFIX')
    exit()
    
DIR  = parameters[0]
PREF = parameters[1]
LIST_TRUE = parameters[2]
DIR_TRUE  = parameters[3]
DIR_NNI   = parameters[4]
SUFFIX    = parameters[5]

gene_file    = DIR+'/'+PREF+'.genes.txt'
adj_file     = DIR+'/'+PREF+'.adjacencies.txt'
rec_file     = DIR+'/'+PREF+'.reconciliations.newick'
adjtree_file = DIR+'/'+PREF+'.adjacencyTrees.newick'
param_file   = DIR+'/'+PREF+'_DeCoSTAR_parameters'+SUFFIX

rf                                = RF(LIST_TRUE,DIR_TRUE,DIR_NNI)
(dup_cost,loss_cost,hgt_cost)     = extract_rec_costs(param_file)
(nb_dup,nb_loss,nb_hgt,rec_score) = reconciliation_score(rec_file,dup_cost,loss_cost,hgt_cost)
(nb_gain,nb_break,DeCo_score)     = DeCo_score(adjtree_file)
linearity_score = linearity_score(gene_file, adj_file)

print(PREF+'\t'+str(rf)+'\t'+str(nb_dup)+'\t'+str(nb_loss)+'\t'+str(nb_hgt)+'\t'+str(rec_score)+'\t'+str(nb_gain)+'\t'+str(nb_break)+'\t'+str(DeCo_score)+'\t'+str(linearity_score))
