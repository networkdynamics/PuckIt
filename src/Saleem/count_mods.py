'''
extract the moderator count for each sub
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

def get_mod_count(sub_name):
    sub_path = os.path.join(data_dir, sub_name)
    file_name = 'moderators.json'
    file_path = os.path.join(sub_path, file_name)
    try:
        with open(file_path, 'r') as fp:
            content = json.load(fp)
            print len(content['data']['children'])
    except IOError:
        print 0
    return



for sub in all_subs:
    get_mod_count(sub)
