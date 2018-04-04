__author__ = 'Caitrin'
from collections import defaultdict
import sys
import csv
import json

def construct_network_graph(sub_dir):
    id_author = {}
    comment_file = sub_dir + "reddit_comments.txt"
    with open(comment_file, "rb") as infile:
        for line in infile:

            data = json.loads(line)

            id_author[data["id"]] = (data["parent_id"], data["author"])

    print len(id_author)
    user_pairs = defaultdict(lambda: 0)
    for post_id in id_author:
        parent_id = id_author[post_id][0]

        if "t3" not in parent_id[:3]:

            if parent_id[3:] in id_author:
                # where first is always the parent
                parent = id_author[parent_id[3:]][1]
                child = id_author[post_id][1]
                if "[deleted]" in parent or "[deleted]" in child:
                    continue
                user_pairs[(parent, child)] += 1


    network_file = sub_dir + "network_file.txt"

    with open(network_file, "wb") as outfile:

        csvwriter = csv.writer(outfile, delimiter = ",")
        for pairing in user_pairs:
            csvwriter.writerow([pairing[0], pairing[1], user_pairs[pairing]])


sub_dir = sys.argv[1]

construct_network_graph(sub_dir)

