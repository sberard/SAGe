import script_tree,os

file_headers = open("data/headers.nex","r").readlines()

correspondance = {}
for line in file_headers:
    words = line.split()
    if len(words) == 1:
        family = words[0].split("_")[0]
        if words[0].find("run1") >= 0:
            correspondance[family] = {}
            good_run = True
        else:
            good_run = False
    else:
        mrbayes_name = words[0]
        new_name = words[1].split("_")[0]+"@"+family+"_"+words[1].split("_")[1]
        if good_run:
            correspondance[family][mrbayes_name] = new_name
    #print line.strip(),good_run,family,correspondance[family].keys()

all_families = os.listdir("results")

for f in all_families:
    ale_file = open("results/"+f+"/"+f+"_run1.gtrees.ale","r").readlines()
    new_ale_file = open("all_families/"+f+".ale","w")
    for line in ale_file:
        if line[0] == "(":
            tree = script_tree.readTree(line)
            root = script_tree.getRoot(tree)
            leaves = script_tree.getLeaves(tree,root)
            for l in leaves:
                #print "family",f,"leaf",l,script_tree.getName(tree,l)
                script_tree.setName(tree,l,correspondance[f][script_tree.getName(tree,l)])
            new_ale_file.write(script_tree.writeTree(tree,root,False)+"\n")
        else:
            new_ale_file.write(line)

all_families = os.listdir("../../simulations/data_D10T10L20I10T10/S/")
for line in all_families:
    #print line.strip()[-5:]
    if line.strip()[-12:] == "pruned.fasta":
        family = line.split("_")[0]
        if not correspondance.has_key(family):
            genes = []
            file_family = open("../../simulations/data_D10T10L20I10T10/S/"+line.strip(),"r").readlines()
            for line2 in file_family:
                if line2[0] == ">":
                    genes.append(line2[1:].strip().split("_")[0]+"@"+family+"_"+line2[1:].strip().split("_")[1])
            output = open("all_families/"+family+".tree","w")
            output.write("(")
            for g in genes[:-1]:
                output.write(g+",")
            output.write(genes[-1]+");\n")
            print "ALEobserve all_families/"+family+".tree"
                    
                    
                    
                    
