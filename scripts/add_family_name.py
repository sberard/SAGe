import sys,string,script_tree

parameters = sys.argv[1:]

for p in parameters:
    name_family = p.split("/")[-1].split("_")[0]
    tree = script_tree.readTree(open(p,"r").readline())
    root = script_tree.getRoot(tree)
    leaves = script_tree.getLeaves(tree,root)
    for l in leaves:
        name = script_tree.getName(tree,l)
        new_name = name.split("_")[0]+"@"+name_family+"_"+name.split("_")[1]
        script_tree.setName(tree,l,new_name)
    output = open(p,"w")
    output.write(script_tree.writeTree(tree,root,False)+"\n")


    