'''
extract the description metadata for each sub
'''

import os
import time
import requests
import json
import sys

sample = sys.argv[1]

index = '2'
if sample == 'small':
    index = '1'

fields = ['allow_discovery', 'banner_size', 'collapse_deleted_comments', 'comment_score_hide_mins', 'link_flair_enabled', 'suggested_comment_sort', 'user_flair_enabled_in_sr', 'wiki_enabled', 'description_html', 'public_description_html', 'submit_text_html'] 
field_index = int(sys.argv[2] )

sub_names = '/home/ndg/users/hsalee/PuckIt/resources/'+sample+'_sample.txt'
data_dir = '/home/ndg/projects/shared_datasets/PuckIt/sample'+index+'/data'

def change(k):
    if k == None:
        return "NULL"
    if k == True:
        return 1
    if k == False:
        return 0
    return k


with open(sub_names, 'r') as fin:
    all_subs = fin.readlines()
all_subs = [x.strip() for x in all_subs]
all_subs = sorted(all_subs, key=lambda s: s.lower())

def get_meta_count(sub_name):
    sub_path = os.path.join(data_dir, sub_name)
    file_name = 'about.json'
    file_path = os.path.join(sub_path, file_name)
    try:
        with open(file_path, 'r') as fp:
            content = json.load(fp)
        data = content['data']
        
        a = data[fields[field_index]]
        if field_index > 7:
            try:
                a = len(a)
            except TypeError:
                a = 0

        a = change(a)
        print a
    except IOError:
        print -1
    return

for sub in all_subs:
    get_meta_count(sub)









    #print data['allow_discovery'], data['banner_size'], data['collapse_deleted_comments'], data['comment_score_hide_mins']

    #print time.strftime("%Y/%m/%d", time.gmtime(data['created_utc'])), data['hide_ads'], data['link_flair_enabled'], data['public_traffic'], data['suggested_comment_sort'], data['user_flair_enabled_in_sr'], data['wiki_enabled']

    #print data['allow_discovery'], data['audience_target'], data['banner_size'], data['collapse_deleted_comments'], data['comment_score_hide_mins'], data['created_utc'], len(data['description_html']), data['hide_ads'], data['link_flair_enabled'], len(data['public_description_html']), data['public_traffic'], data['submit_text_html'], data['suggested_comment_sort'], data['user_flair_enabled_in_sr'], data['wiki_enabled']

