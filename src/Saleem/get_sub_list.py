'''
@uthor: Saleem
Date: April 2, 2018

Get a list of subreddits from all of 2017
'''

#Imports
import os
import time
import json
import gzip
import multiprocessing
from pprint import pprint


data_path = '/home/ndg/projects/shared_datasets/PuckIt/FACITdata/temp'

all_files = sorted(os.listdir(data_path))
all_subs = []

for file_name in all_files:
    print file_name
    file_path = os.path.join(data_path, file_name)

    with open(file_path, 'r') as fin:
        all_lines = fin.readlines()
    
    all_subs.extend(all_lines)
    all_subs = sorted(list(set(all_subs)))


out_file_name = 'all_subs.txt'
with open(out_file_name, 'w') as fp:
    for line in all_subs:
        fp.write(line)


