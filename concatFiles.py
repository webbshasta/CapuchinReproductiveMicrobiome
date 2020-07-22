#!/usr/bin/env python3

#Concatenate files 

import os

#This script takes all files from 2 directories and concatenates them under the same file name
#Files must be unzipped before this script will run

file_paths = {} #initiating an empty dictionary: file names will be the keys and file paths will be the values

for root, dirs, files in os.walk(".", topdown=False): #"." means to start in the current directory
	for f in files:									  #from which the scropt is being run
		if f.endswith(".fastq"):						  #pick the file extension you want here
			if f not in file_paths:					  #if the file name is not a key, make it one
				file_paths[f] = []					  #value of this key is an empty list
			file_paths[f].append(root)				  #changing value to the path to the file

for k, v in file_paths.items():						  #iterating through file names and paths
	print('{} : {}'.format(k,v))					  #file names are keys, paths to that file name
	#print('{} is the path and {} is the fastq file.'.format(k, v))            

for f, paths in file_paths.items():					  #for each file and file associated file paths
	rawReads = []										  #initiate empty list 	
	for p in paths:									  #for each path in the path tuples
		with open(os.path.join(p,f)) as f2:			  #with the path and file names joined opened as file 2	
			rawReads.append(f2.read())					  #append the contents of that file to the empty list
		with open(f, 'w') as f3:					  #with the original file opened for writing as file 3
			f3.write(''.join(rawReads))					  #write the f3 file with the joined contents of the txt list




