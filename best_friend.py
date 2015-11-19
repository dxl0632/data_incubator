# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 11:53:36 2015

@author: Yibin Xu
"""
import sys
sys.path.append("C:\Users\pc\Documents\GitHub\data_incubator")
import cPickle
import os
from collections import Counter
from itertools import combinations

default_dir="C:\Users\pc\Documents\GitHub\data_incubator"
PathNameDict = os.path.join(default_dir, "name_dic.p")
namels_dict = cPickle.load(open(PathNameDict, 'rb'))


def namepair_tp_ls(dict):
    namepair_ls=[]
    for key in dict.keys():
        if dict[key]:
            for singlePicNmlist in dict[key]:
                if singlePicNmlist:
                    singlels=sorted(singlePicNmlist)
                    singlels=[str for str in singlels if len(str)>0]
                    tpls=list(combinations(singlels, 2))
                    namepair_ls.extend(tpls)
    return namepair_ls
    
    
unipair=Counter(namepair_tp_ls(namels_dict))
print len(unipair)

#keys=unipair.keys()
#
#for i in range(100):
#    print keys[i], unipair[keys[i]]

print "List top 100 most showed two person and their showing frequency"
out=[]
for i,w in enumerate(sorted(unipair, key=unipair.get, reverse=True)):
    if i<=100:
        item=(w,unipair[w])
        out.append(item)
        
        
out

outputpath = os.path.join(default_dir, "q3_answer.p")
cPickle.dump(out, open(outputpath, 'wb'))

#def outTopNBF(dict,n):
#    pass
    
    
#Test example
#get a simple dict    

#key=namels_dict.keys()
#testdict={}
#testdict[key[0]]=namels_dict[key[0]]
#testdict[key[1]]=namels_dict[key[1]]
#
#test=namepair_tp_ls(testdict)
#test_bf=Counter(test)


  


#nx.draw(G)