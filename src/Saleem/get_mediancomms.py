'''
@uthor: Saleem
Date: April 3, 2018

Compute median number of comments by each user
'''

#Imports
import os
import time
import json
from numpy import median
from pprint import pprint

data_path = '/home/ndg/projects/shared_datasets/PuckIt/data'
team_file = '/home/ndg/users/hsalee/PuckIt/resources/nhl_teams.txt'
with open(team_file, 'r') as fin:
    all_teams = fin.readlines()
all_teams = [x.strip() for x in all_teams]

def split_data(team_name):
    team_dir = team_name.replace(" ", "_")
    team_path = os.path.join(data_path, team_dir)
    file_name = 'reddit_comments.txt'
    file_path = os.path.join(team_path, file_name)
    with open(file_path, 'r') as fp:
        all_lines = fp.readlines()
    
    auth_dict = {}
    for line in all_lines:
        jobj = json.loads(line)
        auth = jobj['author']
        if auth != "[deleted]":
            if auth != "[removed]":
                if auth not in auth_dict:
                    auth_dict[auth] = 0
                auth_dict[auth] += 1

    print team_dir, len(auth_dict.keys()), int(median(auth_dict.values()))
    return

for team in all_teams:
    split_data(team)


