file_trees = open("iqtrees_reconciliation.newick","r").readlines()
for line in file_trees:
    if line[0] == ">":
        family = line.split()[2]
    else:
        output = open("gene_tree_"+family,"w")
        output.write(line)