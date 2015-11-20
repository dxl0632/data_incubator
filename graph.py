# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 16:34:15 2015

@author: Dao
"""
import sys
#sys.path.append("/Users/Dao/Desktop/GHRepo/data_incubator")

from collections import defaultdict
from itertools import combinations, chain
import cPickle
import os
import networkx as nx
import pandas as pd

from utils import BASE_DIRECTORY

nameDicPath = os.path.join(BASE_DIRECTORY, "name_dic2.p")
name_dic = cPickle.load(open(nameDicPath, 'rb'))



def convertListToTuple(nameList):
    out = []
    for comb in combinations(nameList,2):
        out.append(comb)
    return out


def getGraphFromCaptions(allCaptions):
    """convert a single page's name into a list of paired names"""

    G = nx.Graph()
    
    for nameLists in allCaptions.values():
        for nameList in nameLists:
            nameList = [ i.replace("\r", "") for i in nameList]
            nameTuples = convertListToTuple(nameList)
            if nameList:
                G.add_nodes_from(nameList)
            if nameTuples:
                for nameTuple in nameTuples:
                    firstPerson = nameTuple[0]
                    secondPerson = nameTuple[1]
                    if G.has_edge(firstPerson, secondPerson):
                        G[firstPerson][secondPerson]['weight'] += 1
                    else:
                        G.add_edge(firstPerson, secondPerson, weight = 1)                  
    return G
    
def getSocialDF(G):
    
    allNodes = G.nodes()
    if '' in allNodes:
        G.remove_node('')
    allDegree = G.degree(allNodes, weight = 'weight')
    
    socialGraph = pd.DataFrame({
        "Person" : allDegree.keys(),
        "Degree" : allDegree.values()
    })
    socialGraph.sort(columns = 'Degree', ascending=False, inplace = True)
    return socialGraph

G = getGraphFromCaptions(name_dic)    
socialGraph = getSocialDF(G)

socialGraph.shape
socialGraph.head()

out = []
for i in xrange(100):
    item = (socialGraph['Person'].iloc[i], socialGraph['Degree'].iloc[i])
    out.append(item)
outputPath = os.path.join(BASE_DIRECTORY, 'q1_answer.p')
cPickle.dump(out, open(outputPath, 'wb'))   


result = nx.pagerank(G, alpha=0.85, weight='weight')

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