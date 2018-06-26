'''

Find the number of times mods removed comments
'''

import os
import json
import time
from pprint import pprint

dir_path = '/home/ndg/users/hsalee/PuckIt/resources/nhl_dirs.txt'
data_dir = '/home/ndg/projects/shared_datasets/PuckIt/data'

with open(dir_path, 'r') as fin:
    all_subs = fin.readlines()
all_subs = [x.strip() for x in all_subs]

def get_removed(team_dir):
    team_path = os.path.join(data_dir, team_dir)
    file_name = 'about.json'
    file_path = os.path.join(team_path, file_name)
    data = json.load(open(file_path))
    data = data['data']
    
    try:
        print len(data['submit_text_html'])
    except TypeError:
        print data['submit_text_html']
    #print data['allow_discovery'], data['banner_size'], data['collapse_deleted_comments'], data['comment_score_hide_mins']
    
    #print time.strftime("%Y/%m/%d", time.gmtime(data['created_utc'])), data['hide_ads'], data['link_flair_enabled'], data['public_traffic'], data['suggested_comment_sort'], data['user_flair_enabled_in_sr'], data['wiki_enabled']

    #print data['allow_discovery'], data['audience_target'], data['banner_size'], data['collapse_deleted_comments'], data['comment_score_hide_mins'], data['created_utc'], len(data['description_html']), data['hide_ads'], data['link_flair_enabled'], len(data['public_description_html']), data['public_traffic'], data['submit_text_html'], data['suggested_comment_sort'], data['user_flair_enabled_in_sr'], data['wiki_enabled'] 
    return

for sub in all_subs:
    get_removed(sub)
    
