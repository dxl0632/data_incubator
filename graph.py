# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 16:34:15 2015

@author: Dao
"""
from collections import defaultdict
from itertools import combinations, chain
import cPickle
import os
import networkx as nx
import pandas as pd

from utils import BASE_DIRECTORY

nameDicPath = os.path.join(BASE_DIRECTORY, "name_dic.p")
name_dic = cPickle.load(open(nameDicPath, 'rb'))



def convertListToTuple(nameList):
    out = []
    for comb in combinations(nameList,2):
        out.append(comb)
    return out


def getNameTuples(allCaptions):
    """convert a single page's name into a list of paired names"""
    urlNameTuple = defaultdict(list)
    urls = allCaptions.keys()
    G = nx.Graph()
    
    for url in urls:
        for nameList in allCaptions[url]:
            nameTuple = convertListToTuple(nameList)
            if nameTuple:
                urlNameTuple[url].append(nameTuple)
            G.add_nodes_from(nameList)
            G.add_edges_from(nameTuple)
        urlNameTuple[url] = list(chain(*urlNameTuple[url]))   
    return urlNameTuple, G
    
    
urlNameTuple, G = getNameTuples(name_dic)
G.remove_node('')
allNodes = G.nodes()
allDegree = G.degree(allNodes)

socialGraph = pd.DataFrame({
    "Person" : allDegree.keys(),
    "Degree" : allDegree.values()
})

socialGraph.sort(columns = 'Degree', ascending=False, inplace = True)
socialGraph.shape

out = []
for i in xrange(100):
    item = (socialGraph['Person'].iloc[i], socialGraph['Degree'].iloc[i])
    out.append(item)
outputPath = os.path.join(BASE_DIRECTORY, 'q1_answer.p')
cPickle.dump(out, open(outputPath, 'wb'))   
