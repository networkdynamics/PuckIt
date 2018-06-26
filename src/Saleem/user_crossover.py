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

all_teams = {}

def get_users(team_dir):
    user_set = set()
    team_path = os.path.join(data_dir, team_dir)
    file_name = 'reddit_comments.txt'
    file_path = os.path.join(team_path, file_name)
    with open(file_path, 'r') as fin:
        all_lines = fin.readlines()
    count = 0
    for line in all_lines:
        jobj = json.loads(line)
        author = jobj['author']
        user_set.add(author)
    
    return user_set

for sub in all_subs:
    all_teams[sub] = get_users(sub)

for i in xrange(31):
    sub_auths = all_teams[all_subs[i]]

    rest_auths = set()
    for j in xrange(31):
        if j != i:
            sub_auth = all_teams[all_subs[j]]
            rest_auths |= sub_auth

    rest_auths &= sub_auths
    print float(len(rest_auths))/len(sub_auths)

    



