# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:27:15 2015

@author: jing

split string into names based on "," "and"; remove long items which are not likely to be names
"""
from nameparser import HumanName
import re
import sys
sys.path.append('"C:\Users\pc\Documents\GitHub\Web-scripping\data_incubator"')
import init_text_clean
import cPickle
import os

from utils import BASE_DIRECTORY

#name = "Diane von Furstenberg (good person), Lincoln Center President Jed Bernstein and John."
#name2 = "Lincoln Center President Jed Bernstein"
#name3 = "740 guests attended the New York Philharmonic Opening Night Gala."
#name1 = HumanName(name)

captionPath = os.path.join(BASE_DIRECTORY, "allCaptionsNew.p")
allCaptions = cPickle.load(open(captionPath, 'rb'))
#keys = example.keys()
#example[keys[0]][0]

#remove () and split by ",", "and"
def split_name(string):  
    names = [item.split('(')[0].strip() for item in re.split(',|and', string)]
    return names
    
def first_last_name():
    pass

def remove_sentence():
    pass

def name_dict(caption_dict):
    name_dict = {}
    keys = caption_dict.keys()
    for key in keys:
        name_list_on_page = []
        for caption in caption_dict[key]:
#        print key
            names = split_name(caption)            
            name_list_on_page.append(names)
        name_dict[key] = name_list_on_page
    return name_dict


def caption_parse(caption_dict):
    cleaned_caption = {}
    keys = caption_dict.keys()
    for key in keys:
#        for caption in caption_dict[key]:
#        print key
        clean_caption = init_text_clean.seperate_caption(caption_dict[key])
        cleaned_caption[key] = clean_caption
    return cleaned_caption


def check_num(dict):
    raw_num = 0
    empty_num = 0
    empty_id = []
    keys = dict.keys()
    for key in keys:
        if len(dict[key]) == 0:
            empty_num += 1
            empty_id.append(key)
        raw_num += len(dict[key])
    return raw_num, empty_num, empty_id
         
if __name__ == "__main__":
    cleaned_caption = caption_parse(allCaptions)
    raw_name_dict = name_dict(cleaned_caption)
    
    
 ####check each name list length
#def name_string_length(namestr):
#    return len(namestr)

def name_length_list(dict):
    keys=dict.keys()
    nameLengths=[]
    for key in keys:
        if dict[key]:
            for singlePicNmlist in dict[key]:
                if singlePicNmlist:
                    for nmStr in singlePicNmlist:
                        nameLengths.append(len(nmStr))
    return nameLengths

nm_lens=name_length_list(raw_name_dict)

nm_lens_np=np.array(nm_lens)


fig = matplotlib.pyplot.gcf()
fig.set_size_inches(4, 4,forward=True)
plt.hist(nm_lens_np, bins=50)
plt.title("Name String length distribution")
plt.xlabel("Name String Length")
plt.ylabel("Frequncy")
plt.show()  

print "total number of name strings:" 
print len(nm_lens)
print "total number of name strings length>200:"
print len([s for s in nm_lens if s>200])
print "total number of name strings length>100:"
print len([s for s in nm_lens if s>100])
print "total number of name strings length>80:"
print len([s for s in nm_lens if s>80])
print "total number of name strings length>50:"
print len([s for s in nm_lens if s>50])
print "total number of name strings length>30:"
print len([s for s in nm_lens if s>30])
