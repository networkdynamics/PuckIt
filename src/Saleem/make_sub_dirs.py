import os

data_path = '/home/ndg/projects/shared_datasets/PuckIt/sample2/data'
subs_file = '/home/ndg/users/hsalee/PuckIt/resources/large_sample.txt'

with open(subs_file, 'r') as fin:
    all_subs = fin.readlines()

all_subs = [x.strip() for x in all_subs]

def make_dir(sub):
    print sub
    sub_path = os.path.join(data_path, sub)
    if not os.path.exists(sub_path):
        os.makedirs(sub_path)
    return

for sub in all_subs: 
    make_dir(sub)

