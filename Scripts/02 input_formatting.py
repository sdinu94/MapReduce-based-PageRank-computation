#!/usr/bin/env python

import sys

num_of_nodes=0

#Identify Nodes and Connected Nodes
def parser(line):
    l = line.strip().split("\t")
    parent_node = l[0]
    child_node = l[1]
    list  =  [parent_node,child_node]
    return list

input=[]

#Count total number of nodes in the given input files
for line in sys.stdin:
    num_of_nodes += 1
    input.append(line)

#Set an initial page rank to every node as 1/(total no. of nodes) so that sum of page rank of all nodes is 1
for line in input:
    initial_pr = float(1) / (num_of_nodes)
    l = parser(line)
    op = str(l[0]) + "\t" + str(initial_pr) + "," + str(l[1]) + "\n"
    sys.stdout.write(op)