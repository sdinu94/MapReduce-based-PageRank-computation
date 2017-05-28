#!/usr/bin/env python

import sys

#Identify Node and its PageRank alone
def parser(line):
    l = line.strip().split("\t")
    node_num = l[0]
    value = l[1]
    value = value.split(",")
    pr = value[0]
    list = [node_num, pr]
    return list

map = {}
sort_map = {}

#Map PageRank to its respective node by creating a dictionary
for line in sys.stdin:
    l = parser(line)
    map[int(l[0])] = float(l[1])

#Sort by Node number
sort_map=sorted(map)

#Write sorted output
for line in sort_map:
    op = str(line) + "\t" + str(map[line]) + "\n"
    sys.stdout.write(op)