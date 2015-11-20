# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 12:41:21 2015

@author: pc
"""

import networkx as nx
import sys
sys.path.append('C:\Users\pc\Documents\week1\data_incubator')
import cPickle
import os
from utils import BASE_DIRECTORY
import itertools
import pandas as pd 
import numpy as np

outputPath = os.path.join(BASE_DIRECTORY, 'name_dic.p')
name_dic = cPickle.load(open(outputPath, 'rb'))  
graph = nx.Graph()
for key in name_dic.keys():
    for name_list in name_dic[key]:        
        graph.add_nodes_from(name_list)
        graph.add_edges_from(list(itertools.combinations(name_list, 2)))
    
graph.remove_node('')
result = nx.pagerank(graph, alpha=0.85)

num = np.percentile(result.values(), (109599./109699.)*100)
keys_top = np.array(result.keys())[result.values()> num][0:100]
value_top = np.array(result.values())[result.values()> num][0:100]
pd.DataFrame(value_top).describe()

out = []
for i in xrange(100):
    item = (keys_top[i], value_top[i])
    out.append(item)
    
outputPath = os.path.join(BASE_DIRECTORY, 'q2_answer.p')
cPickle.dump(out, open(outputPath, 'wb'))   