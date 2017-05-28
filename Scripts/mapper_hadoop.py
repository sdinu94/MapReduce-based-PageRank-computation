#!/usr/bin/env python

import sys

#Identify Node, its PageRank and their Connected Nodes
def parser(line):
    l = line.strip().split("\t")
    assert len(l)==2
    node_num = l[0]
    value = l[1]
    value = value.split(",")
    pr=value[0]
    connected_nodes = map(int, value[1:])
    list  =  [node_num,pr,connected_nodes]
    return list

#Pass PageRank to Connected Nodes
def mapper(l):
    maps={}
    if len(l[2])==0:
        pgrk=l[1]
        maps[l[0]]=pgrk

    for node in l[2]:
        pgrk=float(l[1]) / len(l[2])
        maps[node]=pgrk

    for key, values in maps.iteritems():
        sys.stdout.write(str(key)+"\t"+str(values)+"\n")

#Pass along graph structure
for line in sys.stdin:
    l = parser(line)
    graphstruct = str(l[0]) + "\t" + str(l[1])
    graphstruct += "," + (','.join(map(str, l[2])))+"\n"
    sys.stdout.write(graphstruct)
    mapper(l)
