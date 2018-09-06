#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from sys import argv
from ete3 import Tree, faces, TreeStyle, NodeStyle

 
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
def parse_conflit(file):
    dict_conflits=dict()
    file=open(file,"r")
    #Première ligne c'est l'arbre
    line=file.readline()
    t = Tree(line)
    #Les autres lignes ce sont les couples noeud/ nb de conflits --> dico dict_conflits
    #Récupération du nb MAX de conflit pour l'échelle de couleur
    MAX=0
    for line in file:
        element = line.split()
        cle = element[0]
        data = element[1]
        if int(data)>MAX:
            MAX=int(data)
        dict_conflits[cle] = data
    #print dict_conflits
    file.close()
    return t,dict_conflits,MAX

#Définition de l'affichage des noeuds
def layout(node):
    N = faces.TextFace(node.cname, fsize=8, fgcolor="black")
    faces.add_face_to_node(N, node, 0, position="branch-top")


#Lecture du nom de fichier passé en paramètre
filename=argv[1]

#Création de l'arbre et du dictionnaire
t,dict_conflits,MAX=parse_conflit(filename)
#print "MAX=",MAX

#Gestion du degradé de couleur AU LIEU DE MX ON PEUT UTILISER LE MÊME NB POUR TTES LES EXPÉ
jaune = (255, 255, 0)
vert = (0, 255, 0)
rouge = (255, 0, 0)
deg=echelle(vert, rouge, int(MAX)+1)

#Crée un champs 'cname' à chaque noeud de l'arbre qui récupère le nb de conflit 
for n in t.traverse():
    style = NodeStyle()
    if n.is_leaf():
        s=dict_conflits.get(n.name)
    else:
        i = int(n.support)
        s=dict_conflits.get(str(i))
    n.add_features(cname=s)
    style["vt_line_type"] = 0 # 0 solid, 1 dashed, 2 dotted
    style["hz_line_width"] = 5
    style["hz_line_type"] = 0
    style["hz_line_color"] = '#%02x%02x%02x' % deg[int(s)]
    n.img_style=style
    
#Définition du style l'arbre
ts = TreeStyle()
ts.layout_fn=layout
ts.show_leaf_name = True
ts.show_branch_support = False

#Écriture de l'arbre dans un fichier
t.render(filename+".png", w=183, units="mm", tree_style=ts)