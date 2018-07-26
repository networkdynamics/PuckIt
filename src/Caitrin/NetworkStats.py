__author__ = 'Caitrin'
from collections import defaultdict
import sys
import csv
import json
import networkx as nx
#import community

def construct_edgelist(sub_dir):
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


    network_file = sub_dir + "edgelist.txt"

    with open(network_file, "wb") as outfile:

        csvwriter = csv.writer(outfile, delimiter = ",")
        for pairing in user_pairs:
            csvwriter.writerow([pairing[0], pairing[1], user_pairs[pairing]])


def construct_networkx_graph(sub_dir):
    edgelist_file = sub_dir + "edgelist.txt"
    G = nx.read_edgelist(edgelist_file, delimiter=",", create_using=nx.DiGraph(), data=(('weight',int),))
    return G

def get_clustering_coefficient(G):
    GU = G.to_undirected()

    return nx.average_clustering(GU)

def get_assortativity_coef(G):
    return nx.degree_assortativity_coefficient(G, x='in', y='out', weight='weight')

def get_attribute_coef(G):
    return nx.attribute_assortativity_coefficient(G, 'weight')

def get_p_corr_coef(G):
    return nx.degree_pearson_correlation_coefficient(G, x='in', y='out', weight='weight')

def get_neighbour_degree(G):
    return nx.average_neighbor_degree(G, source='in', target='out', weight='weight')

def get_comm(G):
    GU = G.to_undirected()
    return nx.communicability(GU)

def get_clique_size(G):
    GU = G.to_undirected()
    return nx.graph_clique_number(GU)

def get_number_of_cliques(G):
    GU = G.to_undirected()
    return nx.graph_number_of_cliques(GU)

def get_triangles(G):
    GU = G.to_undirected()
    return nx.triangles(GU)

def get_transitivity(G):
    return nx.transitivity(G)

def get_is_strongly_connected(G):
    return nx.is_strongly_connected(G)

def get_number_strongly_connected_components(G):
    return nx.number_strongly_connected_components(G)

def get_is_weakly_connected(G):
    return nx.is_weakly_connected(G)

def get_number_weakly_connected_components(G):
    return nx.number_weakly_connected_components(G)

#need to make undirected
def get_number_connected_components(G):
    GU = G.to_undirected()
    return nx.number_connected_components(GU)

#def get_modularity(G):
#    part = community.best_partition(G)
#    mod = community.modularity(part,G)


sub_dir = sys.argv[1]

#construct_edgelist(sub_dir)

func_list = [get_clustering_coefficient, get_assortativity_coef, get_p_corr_coef, get_clique_size, get_number_of_cliques, get_transitivity, get_is_strongly_connected, get_is_weakly_connected, get_number_strongly_connected_components, get_number_weakly_connected_components]
for func in func_list:
    try:
        res = func(G)
        print [subreddit, func.__name__, res].join(", ")
    except:
        print "could not compute ", func.__name__


G = construct_networkx_graph(sub_dir)
#print "subreddit", "clustering", "assortativity", "pearson_corr_coef", "clique_size", "number_of_cliques", "transitivity", "is_strongly_connected", "is_weakly_connected", "number_strong_comp", "number_weak_comp"
#print sub_dir.split("/")[-2], get_clustering_coefficient(G), get_assortativity_coef(G), get_p_corr_coef(G), get_clique_size(G), get_number_of_cliques(G), get_transitivity(G), get_is_strongly_connected(G), get_is_weakly_connected(G), get_number_strongly_connected_components(G), get_number_weakly_connected_components(G)