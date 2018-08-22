import multiprocessing
import os
from pprint import pprint

base_path = '/home/ndg/projects/shared_datasets/PuckIt/sample2/data/'
sub_file = '/home/ndg/users/hsalee/PuckIt/resources/large_sample.txt'
with open(sub_file, 'r') as fin:
    all_subs = fin.readlines()
all_subs = sorted([x.strip() for x in all_subs], key=lambda s: s.lower())


def get_sub(sub):
    print sub
    sub_path = os.path.join(base_path, sub)
    sub_files = sorted(os.listdir(sub_path))
    sub_files = [x for x in sub_files if "reddit_post" in x]
    if sub_files:
        sub_files = [os.path.join(sub_path, x) for x in sub_files]
        with open(os.path.join(sub_path, 'reddit_posts.txt'), 'w') as fout:
            for sub_file in sub_files:
                with open(sub_file, 'r') as fin:
                    fout.write(fin.read())
                os.remove(sub_file)
    return

def mp_sampler():
    p = multiprocessing.Pool(20)
    p.map(get_sub, all_subs)

if __name__ == '__main__':
    mp_sampler()
