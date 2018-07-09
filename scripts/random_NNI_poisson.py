import sys,script_tree,numpy

parameters = sys.argv[1:]

if len(parameters) != 2:
    print "usage: python random_NNI_poisson.py INPUT_TREE MEAN"
    exit()

tree_file = open(parameters[0],"r").readlines()
i = 0
while tree_file[i] == ">":
    i = i + 1
tree = script_tree.readTree(tree_file[i])
nodes = script_tree.getNodes(tree)

numer_of_NNI = numpy.random.poisson(float(parameters[1]))

for i in range(numer_of_NNI):
    random_node = nodes[int(numpy.random.random(1)[0]*len(nodes))]
    script_tree.NNI(tree,random_node)

root = script_tree.getRoot(tree)
print script_tree.writeTree(tree,root,False)

