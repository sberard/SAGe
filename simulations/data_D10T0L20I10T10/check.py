import os,string

gene_tree = {}
gene_trees_files = os.listdir("G/Gene_trees/")
for file_name in gene_trees_files:
    if string.find(file_name,"pruned") >= 0:
        gene_tree[file_name.split("_")[0]] = len(open("G/Gene_trees/"+file_name,"r").readline())

#print gene_tree.keys()

sequences = {}
sequence_trees_files = os.listdir("S/")
for file_name in sequence_trees_files:
    if string.find(file_name,"pruned") >= 0:
        sequences[file_name.split("_")[0]] = len(open("S/"+file_name,"r").readlines())
        

for g in gene_tree.keys():
    if not sequences.has_key(g):
        print g,gene_tree[g]
print len(gene_tree.keys()),len(sequences.keys())
                                
                                
                                
                                