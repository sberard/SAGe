import sys,string

parameters = sys.argv[1:]

for p in parameters:
    name_family = p.split("/")[-1].split("_")[0]
    lines = open(p,"r").readlines()
    output = open(p+"_modified","w")
    for line in lines:
        if line[0] == ">":
            name = line[1:]
            new_name = name.split("_")[0]+"@"+name_family+"_"+name.split("_")[1]
            output.write(">"+new_name)
        else:
            output.write(line)

    output = open(p+"_modified.phylip","w")
    nb_taxa = 0
    nb_sites = 0
    for line in lines:
        if line[0] == ">":
            nb_taxa = nb_taxa + 1
            nb_sites = 0
        else:
            nb_sites = nb_sites + len(line.strip())
    output.write(str(nb_taxa)+ " " + str(nb_sites))
    for line in lines:
        if line[0] == ">":
            output.write("\n")
            name = line[1:]
            new_name = name.split("_")[0]+"@"+name_family+"_"+name.split("_")[1].strip()
            output.write(new_name + " ")
        else:
            output.write(line.strip())
    output.write("\n")

    