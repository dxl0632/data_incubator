# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 11:27:19 2015

@author: pc
"""

import re

str ="A, B, C, and D Smith"

def name_split(str):
    if 'and' in str or ',' in str:
        str2=str.replace('and', '')
        
        lastname=str2.rsplit(None, 1)[-1]
        #cut the last word
        str2.rsplit(' ', 1)[0]
        
        namelist1=str2.split(',')        

        namelist2=[x.strip()+' '+lastname for x in namelist1]
        return namelist2
    else:
        return str

namelist=name_split(str)
namelist

namelist=name_split("bingyi yang")
namelist
    
