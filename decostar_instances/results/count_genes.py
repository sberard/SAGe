import sys

parameters = sys.argv[1:]

file_genes = parameters[0]
species = parameters[1]
nb = 0

lines = open(file_genes).readlines()
for line in lines:
    words = line.split()
    if words[0] == species:
        nb = nb + 1

print nb
    