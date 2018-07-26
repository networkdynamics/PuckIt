'''
@uthor: Saleem
Date: April 3, 2018

Split comments that belong to the NHL subreddits
'''

#Imports
import os
import time
import json
from pprint import pprint


data_path = '/home/ndg/projects/shared_datasets/PuckIt/sample1/temp'
out_path = '/home/ndg/projects/shared_datasets/PuckIt/sample1/data'

all_files = sorted(os.listdir(data_path))
all_files = [os.path.join(data_path, x) for x in all_files]

sub_file = '/home/ndg/users/hsalee/PuckIt/resources/small_sample.txt'
with open(sub_file, 'r') as fin:
    all_subs = fin.readlines()
all_subs = [x.strip() for x in all_subs]

#read all data
data = []
for filepath in all_files:
    print filepath
    with open(filepath, 'r') as fin:
        all_lines = fin.readlines()
    data.extend(all_lines)


def split_data(sub):
    print sub
    sub_path = os.path.join(out_path, sub)
    to_write = []
    for line in data:
        if '"subreddit":"%s",' %(sub) in line:
            to_write.append(line)

    out_file_name = 'reddit_comments.txt'
    out_file_path = os.path.join(sub_path, out_file_name)
    with open(out_file_path, 'w') as fp:
        for line in to_write:
            fp.write(line)
    return

for sub in all_subs:
    split_data(sub)
