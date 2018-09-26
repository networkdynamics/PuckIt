#Imports
import os
from shutil import copyfile

data_path = '/home/ndg/projects/shared_datasets/PuckIt/FACITdata'
out_path = '/home/ndg/projects/shared_datasets/PuckIt/sample2/data'


sub_file = '/home/ndg/users/hsalee/PuckIt/resources/large_sample.txt'
with open(sub_file, 'r') as fin:
    all_subs = fin.readlines()
all_subs = [x.strip() for x in all_subs]
all_subs = sorted(all_subs, key=lambda s: s.lower())

for sub in all_subs:
    print sub
    src_file = os.path.join(data_path, sub+'.json')
    dst_file = os.path.join(out_path, sub, 'about.json')
    copyfile(src_file, dst_file)



