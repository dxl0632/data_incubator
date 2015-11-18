# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:12:29 2015
    
@author: Yibin
"""

from parsingName import parsingName

def shortName(nameList):
    """
    get a list of strings (raw names)
    1. Strip leading and trailing white spaces
    2. If any string(raw name) contains more then two words, 
       then keep the last two words
    3. Parsing the new string and only keep the real first and last names
    4. Return a new list with clean names
    
    Parameters
    ----------
    nameList : a list of raw name
    
    Returns
    -------
    a list of cleaned names

    """
    if nameList:
        newNameList=[]
        for string in nameList:
            string=string.strip()
            if len(string.split()) >= 2:
                string=' '.join(string.split()[-2:])
            newString=parsingName(string)
            newNameList.append(newString)
    else:
        newNameList=nameList
    return newNameList


#Test Example
#string1=['Flower Center President Lin','Yibin Xu','Jing Xia','Joy','Happy']
#string2=['Flower Center President Daoying Lin   ','  Yibin Xu','Jing Xia','Joy','Happy']
#    
#newnamels1=shortName(string1)
#newnamels2=shortName(string2)
#
#print string1
#print newnamels1
#print string2
#print newnamels2
        
            
        
    
    