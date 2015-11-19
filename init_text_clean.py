# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 16:18:23 2015

@author: Yibin
"""
import re

def del_long(string, maxlen):
    """
    Parameters
    ----------
    string : single page caption list
    maxlen
        
    Returns
    -------
    cleaned and seperated SinglePageCap

    """
    if len(string) > maxlen:
        return ''
    else:
        return string
        
   
def seperate_caption(singlePageCap):
    """
    initial cleaning for single page caption:
    1. remove leading and trailing white space
    2. remove empty and long strings
    3. Seperate one capition to several if contains ';'
    
    Parameters
    ----------
    SinglePageCap : single page caption list
        
    Returns
    -------
    cleaned and seperated SinglePageCap

    """
    if singlePageCap:
        for i,s in enumerate(singlePageCap):
            s=del_long(s, 150)
            if len(s)>0:
                s=s.strip()
                parts = re.split(';', s)
                if len(parts) <= 1:
                    singlePageCap[i]  = s
                else:
                    singlePageCap[i]  = parts[0]
                    for extra in parts[1:]:
                        singlePageCap.append(extra)
    return [ls for ls in singlePageCap if len(s)>0]
    
#example
    
#test=["   one; TwO 3.4 5,6; seven.eight; nine,ten   ",
#      "   ONE; two22; Hello; HOHO   ",
#      "yOu;  ; Hello; HOHO   "]
#test_new=seperate_caption(test)
