'''
@uthor: Saleem
Date: April 3, 2018

Split comments that belong to the NHL subreddits
'''

#Imports
import os
import time
import json
from pprint import pprint


data_path = '/home/ndg/users/hsalee/PuckIt/temp'
out_path = '/home/ndg/projects/shared_datasets/PuckIt/data'

all_files = sorted(os.listdir(data_path))
all_files = [os.path.join(data_path, x) for x in all_files]

sub_file = '/home/ndg/users/hsalee/PuckIt/resources/nhl_subs.txt'
with open(sub_file, 'r') as fin:
    all_subs = fin.readlines()
all_subs = [x.strip() for x in all_subs]

team_file = '/home/ndg/users/hsalee/PuckIt/resources/nhl_teams.txt'
with open(team_file, 'r') as fin:
    all_teams = fin.readlines()
all_teams = [x.strip() for x in all_teams]


def split_data(i):
    team_name = all_teams[i]
    team_sub = all_subs[i]
    
    print team_name
    team_dir = team_name.replace(" ", "_")
    team_path = os.path.join(out_path, team_dir)
    
    to_write = []
    for filepath in all_files:
        with open(filepath, 'r') as fin:
            all_lines = fin.readlines()
        for line in all_lines:
            jobj = json.loads(line)
            sub = jobj['subreddit']
            if sub == team_sub:
                to_write.append(line)

    out_file_name = 'reddit_posts.txt'
    out_file_path = os.path.join(team_path, out_file_name)
    with open(out_file_path, 'w') as fp:
        for line in to_write:
            fp.write(line)
    return

for i in xrange(31):
    split_data(i)
