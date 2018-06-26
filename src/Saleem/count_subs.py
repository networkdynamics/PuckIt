'''
extract the subscriber count for each sub
'''


import os
import time
import json
from numpy import median

data_dir = '/home/ndg/projects/shared_datasets/PuckIt/FACITdata'


all_subs = os.listdir(data_dir)
all_subs = sorted(all_subs, key=lambda s: s.lower())

def get_about(file_name):
    file_path = os.path.join(data_dir, file_name)
    with open(file_path, 'r') as fp:
        content = json.load(fp)
    a = content['data']['subscribers']
    if a :
        return a
    else:
        return 0

defaults = '/home/ndg/users/hsalee/PuckIt/resources/default_subs.txt'

with open(defaults, 'r') as fin:
    all_defaults = fin.readlines()

all_defaults = [x.strip() for x in all_defaults]

sub_count = {}
for sub in all_subs:
    sub_count[sub] = get_about(sub)


med = median(sub_count.values())

subs = []

for sub in all_subs:
    if sub not in all_defaults:
        if sub_count[sub] > med:
            subs.append(sub)

for item in subs:
    print item
