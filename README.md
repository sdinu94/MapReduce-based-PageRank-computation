# MapReduce-based-PageRank-computation
A MapReduce based PageRank algorithm implemented in Python. The program runs on Hadoop framework

# Requirements
• Python 2.7

• Cloudera Quickstart VM

# Implementation
• **Driver.py:** This file drives the entire pagerank algorithm. It prompts messages asking for input file location, output file location, directory to be created in Hadoop to store input data, directory to be created in Hadoop to store output, location of python files, python streamer to execute python on Hadoop and number of iterations. Once we specify these, other tasks are invoked in terminal automatically by this driver.

• **Input_Formatting.py:**

	The given input file is in the following format: 	
		Node1<tab>Node12, Node13, Node14…
	
	The input file is transformed to the following format:	
		Node1<tab>IPR1, Node12, Node12, Node14…
	
	Here, IPR1 is the initial page rank of Node 1. This is calculated by 1/ (Total number of nodes)

• **Mapper_Hadoop.py:** Mapper implementation of the algorithm

• **Reducer_Hadoop.py:** Reducer implementation of the algorithm

• **Output_Formatting.py:** 

	The output of Reducer_Hadoop is in the following format:
 		Node1<tab>IPR1, Node12, Node12, Node14…
     
  	This has been converted to the desired format:
 		Node1<tab>PR

# Execution
• Name the input file as input_pagerank.txt

• Place all the .py files in the same folder
	
• In the terminal, execute: python file_location/driver.py

• It will now prompt a series of messages asking for location of respective files

	• Local: Enter input file path: -> Enter the location of input_pagerank.txt which is present in your local. Eg: /user/Desktop/Bigdataproject
	  Do not include ‘/’ in the end
	  
	• Local: Enter output file path: -> Enter the location where you want to store your output. Eg: /user/Desktop/Bigdataproject
	  Do not include ‘/’ in the end
	  
	• Hadoop: Enter input directory path (with directory name): -> Enter the name of the directory in which input file is to be stored. Eg: ip_pagerank	
	  Note: If the directory is already existing, then the directory along with its files will be removed automatically
	        Creation of new directory with more than one level is not possible. Eg: bigdataproj/input – Error will be thrown if the parent directory(bigdataproj) is not created before executing driver.py 

	• Hadoop: Enter output directory path (with directory name): -> Enter the name of the directory in which output file is to be stored. Eg: op_pagerank
	  Note: If the directory is already existing, then the directory along with its files will be removed automatically
		Creation of new directory with more than one level is not possible. Eg: bigdataproj/output – Error will be thrown if the parent directory(bigdataproj2) is not created before executing driver.py

	• Enter location of python files: Store all the .py file in a common folder. Provide the path here. Eg: /user/Desktop/Pythonfiles
	  Do not include ‘/’ in the end

	• Enter path of python streamer: To run the python file in Hadoop environment, a streaming file needs to be executed. Locate the file. The name of the .jar file varies with different environment. Hence, mention the file name along with the extension. Eg: /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.8.0.jar

	• Enter the number of iterations: Fixed number of iterations is chosen as the convergence criteria. Enter an integer to define the convergence criteria. Eg: 10
	
• Once we enter these inputs, the MapReduce algorithm executes for the specified number of iterations

• The final output will be stored in the location specified. The name of the file will be Output.txt

• To view the output in the desired format, use Wordpad (in Windows) to view it. We might not be able to view in the desired format with Notepad
