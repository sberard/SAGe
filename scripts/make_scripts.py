#
#
# construct script to run iqtree on all tree files


import string,sys,math,random,script_tree,os

parameters = sys.argv[1:]
if len(parameters) < 3:
    print "usage: python make_scripts.py simulation_dir output_dir transfer_boolean"
    exit()

simulation_dir = parameters[0]
output_dir = parameters[1]
transfer = parameters[2]

alignment_files = os.listdir(simulation_dir+"/S/")

for alignment_file in alignment_files:
    if string.find(alignment_file,"pruned") >= 0 and string.find(alignment_file,"fasta.") < 0 and string.find(alignment_file,"fasta_") < 0:
        print "python add_family_name_alignments.py "+simulation_dir+"/S/"+alignment_file
        if transfer == "0":
            print "raxmlHPC-SSE3 -m  GTRGAMMA -n "+alignment_file+" -s "+simulation_dir+"/S/"+alignment_file+"_modified -p 5 -f a -x 5 -N autoFC -w "+output_dir
        else:
            print "pb -d "+simulation_dir+"/S/"+alignment_file+"_modified.phylip -dgam 4 -gtr -x 10 2000 "+alignment_file.split("/")[-1].split(".")[0]
            print "cp "+alignment_file.split("/")[-1].split(".")[0]+"* "+output_dir
    
    