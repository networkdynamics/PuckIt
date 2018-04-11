'''

Find the number of times mods removed comments
'''

import os
import json


dir_path = '/home/ndg/users/hsalee/PuckIt/resources/nhl_dirs.txt'
data_dir = '/home/ndg/projects/shared_datasets/PuckIt/data'

with open(dir_path, 'r') as fin:
    all_subs = fin.readlines()
all_subs = [x.strip() for x in all_subs]

def get_removed(team_dir):
    team_path = os.path.join(data_dir, team_dir)
    file_name = 'reddit_comments.txt'
    file_path = os.path.join(team_path, file_name)
    with open(file_path, 'r') as fin:
        all_lines = fin.readlines()
    count = 0
    for line in all_lines:
        if '"body":"[removed]"'in line:
            count+=1
    print team_dir, count
    return

for sub in all_subs:
    get_removed(sub)
