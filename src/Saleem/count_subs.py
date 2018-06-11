'''
extract the subscriber count for each sub
'''


import os
import time
import json


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



z = []
for sub in all_subs:
    z.append(get_about(sub))

z = sorted(z)
for item in z:
    print item
