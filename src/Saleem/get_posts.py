'''
@uthor: Saleem
Date: April 3, 2018

Gather posts that belong to the NHL subreddits
'''

#Imports
import os
import time
import json
import multiprocessing
from pprint import pprint


out_path = '/home/ndg/users/hsalee/PuckIt/temp'
raw_path = '/home/ndg/arc/reddit_submissions'

all_files = ['RS_2016-09', 'RS_2016-10', 'RS_2016-11', 'RS_2016-12', 'RS_2017-01', 'RS_2017-02', 'RS_2017-03', 'RS_2017-04', 'RS_2017-05', 'RS_2017-06', 'RS_2017-07', 'RS_2017-08', 'RS_2017-09', 'RS_2017-10', 'RS_2017-11', 'RS_2017-12', 'RS_2018-01']

sub_file = '/home/ndg/users/hsalee/PuckIt/resources/nhl_subs.txt'
with open(sub_file, 'r') as fin:
    all_subs = fin.readlines()
all_subs = set([x.strip() for x in all_subs])

def get_subs(file_name):
    print file_name
    year = file_name[3:7]
    file_path = os.path.join(raw_path, year, file_name)

    with open(file_path, 'r') as fin:
        all_lines = fin.readlines()


    to_write = []
    for line in all_lines:
        jobj = json.loads(line)
        sub = jobj['subreddit']
        if sub in all_subs:
            to_write.append(line)

    out_file_name = file_name
    out_file_path = os.path.join(out_path, out_file_name)
    with open(out_file_path, 'w') as fp:
        for line in to_write:
            fp.write(line)
    return


#Multiprocessing Pool

def mp_sampler():
    p = multiprocessing.Pool(17)
    p.map(get_subs, all_files)

#Run it

if __name__ == '__main__':
    mp_sampler()
