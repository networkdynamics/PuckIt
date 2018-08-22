'''
extract the subscriber count for each sub
'''


import os
import time
import requests
import json

headers = {"User-Agent": "lets get these pages"}

teampath = '/home/ndg/users/hsalee/PuckIt/resources/small_sample.txt'
data_dir = '/home/ndg/projects/shared_datasets/PuckIt/data'


with open(teampath, 'r') as fin:
    all_teams = fin.readlines()
all_teams = [x.strip() for x in all_teams]

def get_about(team_name):
    team_dir = team_name.replace(" ", "_")
    team_path = os.path.join(data_dir, team_dir)
    file_name = 'moderators.json'
    file_path = os.path.join(team_path, file_name)
    with open(file_path, 'r') as fp:
        content = json.load(fp)
    print len(content['data']['children'])
    return



for team in all_teams:
    get_about(team)
