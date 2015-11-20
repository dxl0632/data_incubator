# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:39:32 2015

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
                    single_set=set(singlePicNmlist)
                    singlels=list(single_set)
                    singlels=[str.strip() for str in singlels if len(str.strip())>0]
                    singlels=sorted(singlels)
                    tpls=list(combinations(singlels, 2))
                    namepair_ls.extend(tpls)
    return namepair_ls
    

def nameTpToList(lstp):
    singleNameLs=[]
    for tp in lstp:
        nmls=list(tp)
        singleNameLs.extend(nmls)
    return singleNameLs
 


namepairs=namepair_tp_ls(namels_dict) 


#Get single name list for cal. degree   
singleNm=Counter(nameTpToList(namepairs))
print "Unique single names: ", len(singleNm)

print "List top 100 most showed directly connected person "
out=[]
for i,w in enumerate(sorted(singleNm, key=singleNm.get, reverse=True)):
    if i<=100:
        item=(w,singleNm[w])
        out.append(item)
  
        
print len(out[:100])
out[:100]



#Get paired name list for cal. best_friends
unipair=Counter(namepairs)
print "Unique name-pairs: ", len(unipair)

print "List top 100 most showed two person and their showing frequency"
out_bf=[]
for i,w in enumerate(sorted(unipair, key=unipair.get, reverse=True)):
    if i<=100:
        item=(w,unipair[w])
        out_bf.append(item)
        
        
print len(out_bf[:100])
out_bf[:100]







