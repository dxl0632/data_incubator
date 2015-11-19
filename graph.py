# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 16:34:15 2015

@author: Dao
"""
from collections import defaultdict
import matplotlib.pyplot as plt
from itertools import combinations, chain

import networkx as nx
import pandas as pd

G = nx.Graph()

G.add_nodes_from(["Daoying Lin", "Yibin Xu", "Jing Xia"])
G.add_edges_from([("Daoying Lin", "Yibin Xu"), ("Jing Xia", "Yibin Xu")]) 
G.add_edge("Daoying Lin", "Jing Xia")
G.add_node("Ren Wang")
G.add_edge("Ren Wang", "Jing Xia")
nx.connected_components(G)
nx.clustering(G)
G.add_node()

nx.draw(G)
nx.draw_random(G)
nx.draw_circular(G)





nameList = ["Daoying Lin", "Yibin Xu", "Jing Xia", "Bingyi Yang"]


testCaption = {
'url1' : [
["Daoying Lin", "Yibin Xu", "Jing Xia", "Bingyi Yang"],
["Daoying Lin", "Yibin Xu", "Jing Xia", "Bingyi Yang"],
["Daoying Lin", "Yibin Xu", "Jing Xia", "Bingyi Yang"]
],
'url2' :  [
["Daoying Lin",  "Bingyi Yang"],
["Jing Xia", "Bingyi Yang"],
["Daoying Lin", "Jing Xia", "Bingyi Yang"]
]                         
}



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
        urlNameTuple[url] = list(chain(*urlNameTuple[url]))      
        G.add_nodes_from(nameList)
        G.add_edges_from(nameTuple)
        
    return urlNameTuple, G
    
urlNameTuple, G = getNameTuples(allCaptions)

allNodes = G.nodes()
allDegree = G.degree(allNodes)

socialGraph = pd.DataFrame({
    "Person" : allDegree.keys(),
    "Degree" : allDegree.values()
})