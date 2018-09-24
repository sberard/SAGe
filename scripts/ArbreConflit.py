#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from sys import argv
from ete3 import Tree, faces, TreeStyle, NodeStyle, CircleFace
import script_tree

PREFIX = argv[1]

species_tree = script_tree.readTree(open(PREFIX+".speciesTree.newick","r").readline())
genes = open(PREFIX+".genes.txt","r").readlines()
adjacencies = open(PREFIX+".adjacencies.txt","r").readlines()

all_species = {}
root = script_tree.getRoot(species_tree)
nodes = script_tree.getNodes(species_tree)
for n in nodes:
    if script_tree.isLeaf(species_tree,n):
        name = script_tree.getName(species_tree,n).split("@")[0]
        script_tree.setName(species_tree,n,name)
    else:
        name = script_tree.getBootstrap(species_tree,n)
    script_tree.setLength(species_tree,n,1)
    all_species[name] = {}

script_tree.ultrametricize(species_tree)
line_tree=script_tree.writeTree(species_tree,root,False)

for line in genes:
    words = line.split()
    if len(words) == 2:
        species = words[1].split("@")[0]
    else:
        species = words[0]
    all_species[species][words[1]] = []

#for n in all_species.keys():
    #print n,len(all_species[n].keys())
    
for line in adjacencies:
    words = line.split()
    gene1 = words[1]
    gene2 = words[2]
    if all_species.has_key(words[0]):
        species = words[0]
    else:
        species = words[1].split("@")[0]
    all_species[species][gene1].append(gene2)
    all_species[species][gene2].append(gene1)

list_elements = []
for n in all_species.keys():
    conflict = 0
    for g in all_species[n].keys():
        conflict = conflict + abs(len(all_species[n][g])-2)
    list_elements.append([n,int(float(conflict)/len(all_species[n].keys())*1000)])



#Pour obtenir un dégradé de couleur
def echelle(color_begin, color_end, n_vals):
    r1, g1, b1 = color_begin
    r2, g2, b2 = color_end
    degrade = []
    etendue = n_vals - 1
    for i in range(n_vals):
        alpha = 1 - i / etendue
        beta = i / etendue
        r = int(r1 * alpha + r2 * beta)
        g = int(g1 * alpha + g2 * beta)
        b = int(b1 * alpha + b2 * beta)
        degrade.append((r, g, b))
    return degrade

#Pour parser le fichier passé en paramètre
def parse_conflit(line_tree,list_elements):
    dict_conflits=dict()
    #file=open(file,"r")
    #Première ligne c'est l'arbre
    #line=file.readline()
    t = Tree(line_tree)
    #Les autres lignes ce sont les couples noeud/ nb de conflits --> dico dict_conflits
    #Récupération du nb MAX de conflit pour l'échelle de couleur
    MAX=0
    for element in list_elements:
        #element = line.split()
        cle = element[0]
        data = element[1]
        if int(data)>MAX:
            MAX=int(data)
        dict_conflits[cle] = data
    #print dict_conflits
    #file.close()
    return t,dict_conflits,MAX

#Définition de l'affichage des noeuds
def layout(node):
    # N = faces.TextFace(node.cname, fsize=8, fgcolor="black")
    # faces.add_face_to_node(N, node, 0, position="branch-top")
    if int(node.cname)>0:
        # Creates a sphere face whose size is proportional to node's
        # feature "weight"
        C = CircleFace(radius=int(node.cname)/5, color="RoyalBlue", style="sphere")
        # Let's make the sphere transparent
        C.opacity = 0.3
        # And place as a float face over the tree
        faces.add_face_to_node(C, node, 0, position="float")

#Lecture du nom de fichier passé en paramètre
#filename=argv[1]

#Création de l'arbre et du dictionnaire
t,dict_conflits,MAX=parse_conflit(line_tree,list_elements)
#print "MAX=",MAX

#Gestion du degradé de couleur AU LIEU DE MX ON PEUT UTILISER LE MÊME NB POUR TTES LES EXPÉ
jaune = (255, 255, 0)
vert = (0, 255, 0)
rouge = (255, 0, 0)
deg=echelle(vert, rouge, int(MAX)+1)

#Crée un champs 'cname' à chaque noeud de l'arbre qui récupère le nb de conflit 
for n in t.traverse():
    style = NodeStyle()
    b=False
    if n.is_leaf():
        s=dict_conflits.get(n.name)
    else:
        i = int(n.support)
        s=dict_conflits.get(str(i))
        if (n.children[0].name=="n236" or n.children[1].name=="n236"):
            b=True
            print "Trouvé \n"
    n.add_features(cname=s)
    n.add_features(color=b)
    #Pour que le noeud ne soit pas matérialisé
    style["size"] = 0
    style["vt_line_type"] = 0 # 0 solid, 1 dashed, 2 dotted
    style["hz_line_width"] = 2
    style["hz_line_type"] = 0
    if b:
        style["hz_line_color"] = '#%02x%02x%02x' % rouge
    else:
        style["hz_line_color"] = '#%02x%02x%02x' % vert
    #style["hz_line_color"] = '#%02x%02x%02x' % deg[int(s)]
    #Pour l'affichage du point dont le diamètre dépend du nb d'erreur
    # if int(s)>0:
    #     style["fgcolor"] = "red"
    #     style["size"] = 15*int(s)/MAX
    n.img_style=style
    
#Définition du style l'arbre
ts = TreeStyle()
ts.layout_fn=layout
ts.show_leaf_name = True
ts.show_branch_length = False
ts.show_branch_support = False

#Écriture de l'arbre dans un fichier
t.render(PREFIX+".png", w=183, units="mm", tree_style=ts)
