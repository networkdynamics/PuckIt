'''
extract the number of unique user count for each sub
'''


import os
import time
import requests
import json
import sys

sample = sys.argv[1]

index = '2'
if sample == 'small':
    index = '1'

sub_names = '/home/ndg/users/hsalee/PuckIt/resources/'+sample+'_sample.txt'
data_dir = '/home/ndg/projects/shared_datasets/PuckIt/sample'+index+'/data'


with open(sub_names, 'r') as fin:
    all_subs = fin.readlines()
all_subs = [x.strip() for x in all_subs]
all_subs = sorted(all_subs, key=lambda s: s.lower())

def get_removed_count(sub_name):
    sub_path = os.path.join(data_dir, sub_name)
    file_name = 'reddit_comments.txt'
    file_path = os.path.join(sub_path, file_name)
    count = 0
    with open(file_path, 'r') as fp:
        for line in fp:
	    if '"body":"[removed]"'in line:
                count+=1
    print count
    return



for sub in all_subs:
    get_removed_count(sub)
