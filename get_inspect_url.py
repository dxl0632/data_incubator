# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 19:18:23 2015

@author: Yibin
"""
import re
import sys
sys.path.append("C:\Users\pc\Documents\GitHub\Web-scripping\data_incubator")
import os
import cPickle
import init_text_clean
#import requests
#from requests.exceptions import  ConnectionError
#from bs4 import BeautifulSoup
from utils import BASE_DIRECTORY
import init_text_clean 

#allCaptions = cPickle.load(open('allCaptions.p', 'rb'))

#keys = allCaptions.keys()
#example[keys[0]][0]

captionPath = os.path.join(BASE_DIRECTORY, "allCaptionsNew.p")
allCaptions = cPickle.load(open(captionPath, 'rb'))

#Below function used for quality check
def check_dict(dictionary):
    total_element=len(dictionary)
    none_element=0
    value_element=0
    keys=dictionary.keys()
    for key in keys:
       if dictionary[key]:
           value_element += 1
       else:
           none_element += 1
    return total_element,none_element,value_element


    
def value_caption_hist(dict):
    capdict_tot={}
    capdict_valid={}
    keys=dict.keys()
    pageCaptionTot=0
    for key in keys:
       if dict[key]:
          pageCaptionTot=len(dict[key])
          pageValCaptionCnt=0
          for caption in dict[key]:
              if caption:
                  pageValCaptionCnt += 1
       else:
           pageCaptionTot=0
           pageValCaptionCnt=0
       capdict_tot[key]=pageCaptionTot
       capdict_valid[key]=pageValCaptionCnt
    return capdict_tot,capdict_valid
#####Quality Check############################

if __name__ == "__main__":
    tot_hist,valid_hist=value_caption_hist(allCaptions)
    tot=[tot_hist[key] for key in tot_hist.keys()]
    valid=[valid_hist[key] for key in valid_hist.keys()]
    
import numpy as np
total=np.array(tot)
validc=np.array(valid)
print total.mean()
print validc.mean()

print len(total)
print len(validc)

#%matplotlib inline #skip open another windows for plot and add plots inline
import matplotlib
import seaborn as sns
#make images bigger
#matplotlib.rcParams['savefig.dpi'] =2 *  matplotlib.rcParams['savefig.dpi']
import matplotlib as mpl
import matplotlib.pyplot as plt


 # Histogram for total caption and valid-value caption
data = np.random.gamma(4.5, 1.0, 10000)
plt.hist(total, bins=50)
plt.title("Number of Total Captions Each Page distribution (1192 pages)")
plt.xlabel("Value")
plt.ylabel("Frequncy")
plt.show()  
    
data = np.random.gamma(4.5, 1.0, 10000)
plt.hist(validc, bins=50)
plt.title("Number of Valued-Captions Each Page distribution (1192 pages)")
plt.xlabel("Value")
plt.ylabel("Frequnc")
plt.show()  

#print len([x for x in validc if x<=30])        
#147
           
####dump url which need to be investigated for more captions
inspectUrl=[key for key in valid_hist.keys() if valid_hist[key]<=30]
#print len(inspectUrl) #147
outputPath = os.path.join(BASE_DIRECTORY, 'inspect_url.p')
cPickle.dump(inspectUrl, open(outputPath, 'wb'))           
    