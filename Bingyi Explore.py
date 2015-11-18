# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 11:27:19 2015

@author: Bingyi
"""

"""
import re

str ="A, B, C, and D Smith"

def name_split(str):
    if 'and' in str or ',' in str:
        str2=str.replace('and', '')
        
        lastname=str2.rsplit(None, 1)[-1]
        #cut the last word
        str2=str2.rsplit(' ', 1)[0]
        print "str2={%s}" % str2
        
        namelist1=str2.split(',')        

        namelist2=[x.strip()+' '+lastname for x in namelist1]
        return namelist2
    else:
        return str

namelist=name_split(str)
namelist

namelist=name_split("bingyi yang")
namelist
"""

inputNameList=["A", "B", "C D", "E", "F", "G H", "I", "J K"]

# output: ['A D', 'B D', 'C D', 'E H', 'F H', 'G H', 'I K', 'J K']

def AppendLastName(inputNameList):
    numWordsList=[x.strip().count(' ')+1 for x in inputNameList]
    print numWordsList
    
    currIndividual=0
    LastNames=[]
    for x  in numWordsList:
        if x>1:
            LastNames += inputNameList[currIndividual].split()[1]
        currIndividual+=1
    #print LastNames      
    
    currIndividual=0
    outputNameList=[]
    for x  in numWordsList:
        if x==1:
            thisName=inputNameList[currIndividual]+" "+LastNames[0]
        else:
            thisName=inputNameList[currIndividual]
            del LastNames[0]
        #print thisName
        outputNameList+=[thisName]
        currIndividual+=1
    return outputNameList      

print AppendLastName(inputNameList)

        
        
        
        
    



    
