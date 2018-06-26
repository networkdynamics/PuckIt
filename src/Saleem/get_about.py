'''
Get the about.json for each subreddit
'''

import os
import time
import requests
import json

headers = {"User-Agent": "lets get these pages"}

sub_path = '/home/ndg/users/hsalee/PuckIt/resources/all_subs.txt'
data_dir = '/home/ndg/projects/shared_datasets/PuckIt/FACITdata'

with open(sub_path, 'r') as fin:
    all_subs = fin.readlines()
all_subs = [x.strip() for x in all_subs]


def get_about(sub_name):
    print sub_name
    url = "http://www.reddit.com/r/{}/about.json".format(sub_name)
    resp = requests.get(url, headers=headers)
    if not resp.ok:
        # handle request error, return -1?
        return -1
    content = resp.json()
    file_name = sub_name+'.json'
    file_path = os.path.join(data_dir, file_name)
    with open(file_path, 'w') as fp:
        json.dump(content, fp)
    return


for sub in all_subs:
    get_about(sub)
