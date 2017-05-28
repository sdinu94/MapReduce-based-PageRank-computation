# MapReduce-based-PageRank-computation
A MapReduce based PageRank algorithm implemented in Python. The program runs on Hadoop framework

# Requirements
	• Python 2.7
	• Cloudera Quickstart VM

# Implementation
	• Driver.py – This file drives the entire pagerank algorithm. It prompts messages asking for input file location, output file location, directory to be created in Hadoop to store input data, directory to be created in Hadoop to store output, location of python files, python streamer to execute python on Hadoop and number of iterations. Once we specify these, other tasks are invoked in terminal automatically by this driver.
	• Input_Formatting.py – The given input file is in the following format: 
		Node1<tab>Node12, Node13, Node14…
	We have transformed the input file into the following format:
		Node1<tab>IPR1, Node12, Node12, Node14…
	Here, IPR1 is the initial page rank of Node 1. This is calculated as 1/ (Total number of nodes)
	• Mapper_Hadoop.py – Mapper implementation of the algorithm
	• Reducer_Hadoop.py – Reducer implementation of the algorithm
	• Output_Formatting.py – The output of Reducer_Hadoop is in the following format:
 	Node1<tab>IPR1, Node12, Node12, Node14…
     This has been converted to the desired format:
 	Node1<tab>PR
