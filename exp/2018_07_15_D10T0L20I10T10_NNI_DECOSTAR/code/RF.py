import script_tree,numpy

reference=open("list_gene_trees","r").readlines()

RF = {"025":[],"05":[],"1":[],"2":[],"3":[],"5":[],"7":[],"10":[],"20":[],"30":[],"50":[]}
for line in reference:
    tree_ref = script_tree.readTree(open("../data/gene_trees/"+line.strip(),"r").readline())
    root = script_tree.getRoot(tree_ref)
    for lamb in RF.keys():
        tree_comp = script_tree.readTree(open("../results/NNI/lambda_"+lamb+"/"+line.strip()).readline())
        RF[lamb].append(script_tree.RF(tree_ref,tree_comp))
        
for rf in RF.keys():
    print rf,numpy.mean(RF[rf])