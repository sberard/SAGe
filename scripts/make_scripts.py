#
#
# construct script to run iqtree on all tree files


import string,sys,math,random,script_tree,os

parameters = sys.argv[1:]
if len(parameters) < 2:
    print "usage: python make_scripts.py simulation_dir iqtree_dir"
    exit()

simulation_dir = parameters[0]
iqtree_dir = parameters[1]

alignment_files = os.listdir(simulation_dir+"/S/")

for alignment_file in alignment_files:
    if string.find(alignment_file,"pruned") >= 0 and string.find(alignment_file,"fasta.") < 0:
        print iqtree_dir+"/iqtree -s "+simulation_dir+"/S/"+alignment_file+" -m GTR+G -alrt 1000 -redo"
    
    