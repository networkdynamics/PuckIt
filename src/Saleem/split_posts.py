'''
@uthor: Saleem
Date: April 3, 2018

Split comments that belong to different subs
'''

#Imports
import os
import time
import json
from pprint import pprint
from datetime import datetime


data_path = '/home/ndg/projects/shared_datasets/PuckIt/sample2/temp2'
out_path = '/home/ndg/projects/shared_datasets/PuckIt/sample2/data'

all_files = sorted(os.listdir(data_path))
all_files = [os.path.join(data_path, x) for x in all_files]

sub_file = '/home/ndg/users/hsalee/PuckIt/resources/large_sample.txt'
with open(sub_file, 'r') as fin:
    all_subs = fin.readlines()
all_subs = [x.strip() for x in all_subs]
all_subs = sorted(all_subs, key=lambda s: s.lower())

index = 0
for filepath in all_files:
    index +=1
    print index
    month = "%02d" % (index)
    a = datetime.now()
    data = {}
    for sub in all_subs:
        data[sub] = []

    with open(filepath, 'r') as fin:
        for line in fin:
            jobj = json.loads(line)
            sub = jobj['subreddit']
            data[sub].append(line)

    b = datetime.now()
    print 'data ingested', b-a
    for sub in all_subs:
        out_file_name = 'reddit_post_'+month+'.txt'
        out_file_path = os.path.join(out_path, sub, out_file_name)
        to_write = data[sub]
        if to_write:
            with open(out_file_path, 'w') as fp:
                for line in to_write:
                    fp.write(line)

    print 'data written', datetime.now() - b

