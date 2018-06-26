'''

Find the number of times mods removed comments
'''

import os
import json
from pprint import pprint

dir_path = '/home/ndg/users/hsalee/PuckIt/resources/nhl_dirs.txt'
data_dir = '/home/ndg/projects/shared_datasets/PuckIt/data'

with open(dir_path, 'r') as fin:
    all_subs = fin.readlines()
all_subs = [x.strip() for x in all_subs]

class Comment:
    'Base class for reddit comments'

    def __init__(self, line):
        jobj = json.loads(line)
        self.author = jobj['author']
        self.id = "t1_"+jobj["id"].encode('ascii', 'ignore')
        self.score = jobj["score"]
        self.link_id = jobj["link_id"].encode('ascii', 'ignore')
        self.body = jobj["body"]
        self.parent_id = jobj["parent_id"].encode('ascii', 'ignore')
        self.children = []
    

def get_removed(team_dir):
    team_path = os.path.join(data_dir, team_dir)
    file_name = 'reddit_comments.txt'
    file_path = os.path.join(team_path, file_name)
    with open(file_path, 'r') as fin:
        all_lines = fin.readlines()
    all_lines = [Comment(x) for x in all_lines]
    all_comms = {}
    for comment in all_lines:
        all_comms[comment.id] = comment
    parent_dict = {}
    for comment in all_lines:
        parent_id = comment.parent_id
        if not parent_id in parent_dict:
            parent_dict[parent_id] = []
        parent_dict[parent_id].append(comment.id)

    pprint(parent_dict)
    
    
    return

for sub in all_subs:
    get_removed(sub)
    break
