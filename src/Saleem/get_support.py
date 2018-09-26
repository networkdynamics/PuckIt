import json
import operator
import os

data_path = '/home/ndg/projects/shared_datasets/PuckIt/FACITdata'
all_files = sorted(os.listdir(data_path), key=lambda s: s.lower())

data = {}

for filename in all_files:
    subreddit = filename.split('.')[0]
    print subreddit
    filepath = os.path.join(data_path, filename)
    with open(filepath, 'r') as fp:
        content = json.load(fp)
    try:
        subc = content['data']['subscribers']
        desc = content['data']['description'].lower()

        if 'support group' in desc:
            if subc > 1000:
                data[subreddit] = subc
    except AttributeError:
        continue



sorted_data = sorted(data.items(), key=operator.itemgetter(1), reverse = True)


from pprint import pprint
pprint(sorted_data)

