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
import multiprocessing

data_path = '/home/ndg/projects/shared_datasets/PuckIt/sample2/temp'
out_path = '/home/ndg/projects/shared_datasets/PuckIt/sample2/data'

all_files = sorted(os.listdir(data_path))
num = len(all_files)

sub_file = '/home/ndg/users/hsalee/PuckIt/resources/large_sample.txt'
with open(sub_file, 'r') as fin:
    all_subs = fin.readlines()
all_subs = [x.strip() for x in all_subs]
all_subs = sorted(all_subs, key=lambda s: s.lower())


def split_data(file_name):
    file_path = os.path.join(data_path, file_name)

    print num, '|', all_files.index(file_name)
    data = {}
    for sub in all_subs:
        data[sub] = []

    #sub_path = os.path.join(out_path, sub)

    with open(file_path, 'r') as fin:
        all_lines = fin.readlines()
    for line in all_lines:
        jobj = json.loads(line)
        sub = jobj['subreddit']
        data[sub].append(line)

    for sub in all_subs:
        sub_path = os.path.join(out_path, sub)
        out_file_path = os.path.join(sub_path, file_name)
        with open(out_file_path, 'w') as fp:
            for line in data[sub]:
                fp.write(line)
    return

def mp_sampler():
    p = multiprocessing.Pool(20)
    p.map(split_data, all_files)

if __name__ == '__main__':
    mp_sampler()
