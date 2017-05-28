#!/usr/bin/env python

import sys, os
import os.path

#get file storage location
local_ip_path = raw_input("Local: Enter input file path : ")
local_op_path = raw_input("Local: Enter output file path : ")
hadoop_ip_path = raw_input("Hadoop: Enter input directory path(with directory name) : ")
hadoop_op_path = raw_input("Hadoop: Enter output directory path(with directory name) : ")
py_loc = raw_input("Enter location of python files: ")
streamer_path = raw_input("Enter path of python streamer(with .jar extension): ")

iter=input("Enter the number of Iterations: ")

#Delete the input directory if it is present already
cmd = r"hadoop fs -test -e " + hadoop_ip_path + " && echo $?"
fileCheckip = os.system(cmd)

if int(fileCheckip) == 0:
    cmd = r"hadoop fs -rmr " + hadoop_ip_path
    os.system(cmd)

#Delete the output directory if it is present already
cmd = r"hadoop fs -test -e " + hadoop_op_path + " && echo $?"
fileCheckop = os.system(cmd)

if int(fileCheckop) == 0:
    cmd = r"hadoop fs -rmr " + hadoop_op_path
    os.system(cmd)

#Command line to iterate for the first time - processing raw input file and feeding it as input
cmd= r"python "+ py_loc +"/input_formatting.py < " + local_ip_path + "/input_pagerank.txt > " + local_ip_path + "/input.txt && hadoop fs -mkdir " + hadoop_ip_path + " && hadoop fs -put " + local_ip_path + "/input.txt " + hadoop_ip_path + " && chmod a+x " + py_loc + "/mapper_hadoop.py && chmod a+x " + py_loc + "/reducer_hadoop.py && hadoop jar " + streamer_path + " -input " + hadoop_ip_path + "/input.txt -output " + hadoop_op_path + " -file " + py_loc + "/mapper_hadoop.py -mapper 'python mapper_hadoop.py' -file " + py_loc + "/reducer_hadoop.py -reducer 'python reducer_hadoop.py' && rm -rf " + local_ip_path + "/input.txt"

#Command line to iterate for n-1 times - feeding output of reducer from the previous iteration to the next iteration
for i in range(iter-1):
    cmd+=r"&& hadoop fs -cp -f " + hadoop_op_path + "/part-00000 " + hadoop_ip_path + " && hadoop fs -rmr " + hadoop_op_path + " && hadoop jar " + streamer_path + " -input " + hadoop_ip_path + "/part-00000 -output " + hadoop_op_path + " -file " + py_loc + "/mapper_hadoop.py -mapper 'python mapper_hadoop.py' -file " + py_loc + "/reducer_hadoop.py -reducer 'python reducer_hadoop.py'"

#Formatting the output into desired format
cmd+=r"&& hadoop fs -get "+ hadoop_op_path +"/part\* " + local_op_path + "&& python " + py_loc + "/output_formatting.py < " + local_op_path + "/part-00000 > " + local_op_path + "/output.txt"

#Removing unwanted temporary files
cmd+=r"&& rm -rf " + local_op_path + "/part-00000 && rm -rf " + local_ip_path + "/input.txt"

os.system(cmd)