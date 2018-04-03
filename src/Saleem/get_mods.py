'''
Get the moderators.json for each subreddit
'''

import os
import time
import requests
import json

headers = {"User-Agent": "lets get these pages"}

sub_path = '/home/ndg/users/hsalee/PuckIt/resources/nhl_subs.txt'
teampath = '/home/ndg/users/hsalee/PuckIt/resources/nhl_teams.txt'
data_dir = '/home/ndg/projects/shared_datasets/PuckIt/data'

with open(sub_path, 'r') as fin:
    all_subs = fin.readlines()
all_subs = [x.strip() for x in all_subs]

with open(teampath, 'r') as fin:
    all_teams = fin.readlines()
all_teams = [x.strip() for x in all_teams]

def get_about(sub_name, team_name):
    print team_name
    team_dir = team_name.replace(" ", "_")
    team_path = os.path.join(data_dir, team_dir)
    url = "http://www.reddit.com/r/{}/about/moderators.json".format(sub_name)
    resp = requests.get(url, headers=headers)
    if not resp.ok:
        # handle request error, return -1?
        return -1
    content = resp.json()
    file_name = 'moderators.json'
    file_path = os.path.join(team_path, file_name)
    with open(file_path, 'w') as fp:
        json.dump(content, fp)
    return



for i in xrange(31):
    get_about(all_subs[i], all_teams[i])
