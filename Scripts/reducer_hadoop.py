#!/usr/bin/env python

import sys

d = 0.85

pagerank={}
list=[]

def parser(line):
    l = line.strip().split("\t")
    assert len(l)>=2
    node_num = l[0]
    value = l[1]
    value = value.split(",")
#Insert 0 for Net PageRank if this is the first iteration
    if not node_num in pagerank:
        pagerank[node_num] = 0
#If the element is of the form (Node, PageRank), sum up the PageRank for same Node
    if len(value)==1:
        pagerank[node_num]+=float(value[0])
#If the element represents the entire graph structure, identify Node, PageRank and Connected Node
    else:
        pr=value[0]
        connected_nodes = map(int, value[1:])
        lst  =  [node_num,pr,connected_nodes]
        list.append(lst)

#Apply the formula that reflects the Beta factor
def reducer(line):
    new_pr = (1 - d) + d * pagerank[line[0]]
    line[1]=new_pr
    return line

to_red=[]
red=[]

for line in sys.stdin:
    parser(line)

for line in list:
    l=reducer(line)
    red_op = str(l[0]) + "\t" + str(l[1])
    red_op += "," + (','.join(map(str, l[2])))+"\n"
    sys.stdout.write(red_op)

    
