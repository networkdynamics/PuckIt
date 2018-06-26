'''
@uthor: Saleem
Date: April 2, 2018

Gather comments that belong to the NHL subreddits
'''

#Imports
import os
import time
import json
import gzip
import multiprocessing
from pprint import pprint


out_path = '/home/ndg/projects/shared_datasets/PuckIt/FACITdata/temp'
raw_path = '/home/ndg/arc/reddit'

years = ['2017']

all_files = []

for year in years:
    data_path = os.path.join(raw_path, year)
    files = sorted(os.listdir(data_path))
    files = [x for x in files if 'RC' in x]
    #files = [os.path.join(data_path, x) for x in files]
    all_files.extend(files)

num = len(all_files)

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
        to_write.append(sub)
    to_write = sorted(list(set(to_write)))

    out_file_name = file_name[:-3]
    out_file_path = os.path.join(out_path, out_file_name)
    with open(out_file_path, 'w') as fp:
        for line in to_write:
            fp.write(line)
            fp.write('\n')
    return


#Multiprocessing Pool

def mp_sampler():
    p = multiprocessing.Pool(20)
    p.map(get_subs, all_files)

#Run it

if __name__ == '__main__':
    mp_sampler()
