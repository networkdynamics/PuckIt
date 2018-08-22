'''
Get the moderators.json for each subreddit
'''

import os
import time
import requests
import json

headers = {"User-Agent": "lets get these pages"}

sub_file = '/home/ndg/users/hsalee/PuckIt/resources/large_sample.txt'
data_dir = '/home/ndg/projects/shared_datasets/PuckIt/sample2/data'

with open(sub_file, 'r') as fin:
    all_subs = fin.readlines()
all_subs = [x.strip() for x in all_subs]
all_subs = sorted(all_subs, key=lambda s: s.lower())


def get_mods(sub):
    print sub
    sub_path = os.path.join(data_dir, sub)
    url = "http://www.reddit.com/r/{}/about/moderators.json".format(sub)
    resp = requests.get(url, headers=headers)
    if not resp.ok:
        # handle request error, return -1?
        return -1
    content = resp.json()
    file_name = 'moderators.json'
    file_path = os.path.join(sub_path, file_name)
    with open(file_path, 'w') as fp:
        json.dump(content, fp)
    time.sleep(2)
    return


for sub in all_subs:
    get_mods(sub)
