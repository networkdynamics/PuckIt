'''
@uthor: Saleem
Date: April 2, 2018

Gather comments that belong to subreddits
'''

#Imports
import os
import time
import json
import gzip
import multiprocessing
from pprint import pprint


out_path = '/home/ndg/projects/shared_datasets/PuckIt/sample2/temp'
raw_path = '/home/ndg/arc/reddit'

years = ['2017']

all_files = []

for year in years:
    data_path = os.path.join(raw_path, year)
    files = sorted(os.listdir(data_path))
    files = [x for x in files if 'RC' in x]
    all_files.extend(files)

num = len(all_files)

sub_file = '/home/ndg/users/hsalee/PuckIt/resources/large_sample.txt'
with open(sub_file, 'r') as fin:
    all_subs = fin.readlines()
all_subs = set([x.strip() for x in all_subs])

def get_subs(file_name):
    print file_name, all_files.index(file_name), 'of', num
    year = file_name[3:7]
    file_path = os.path.join(raw_path, year, file_name)

    with gzip.open(file_path, 'r') as fin:
        all_lines = fin.readlines()


    to_write = []
    for line in all_lines:
        jobj = json.loads(line)
        sub = jobj['subreddit']
        if sub in all_subs:
            to_write.append(line)

    out_file_name = file_name[:-3]
    out_file_path = os.path.join(out_path, out_file_name)
    with open(out_file_path, 'w') as fp:
        for line in to_write:
            fp.write(line)
    return


#Multiprocessing Pool

def mp_sampler():
    p = multiprocessing.Pool(20)
    p.map(get_subs, all_files)

#Run it

if __name__ == '__main__':
    mp_sampler()
