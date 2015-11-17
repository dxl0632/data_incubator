# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:27:15 2015

@author: jing

split string into names based on "," "and"; remove long items which are not likely to be names
"""
from nameparser import HumanName
import re
import sys
sys.path.append('C:\Users\pc\Documents\week1\data_incubator')
import init_text_clean
import cPickle

name = "Diane von Furstenberg (good person), Lincoln Center President Jed Bernstein and John."
name2 = "Lincoln Center President Jed Bernstein"
name3 = "740 guests attended the New York Philharmonic Opening Night Gala."
name1 = HumanName(name)

allCaptions = cPickle.load(open('allCaptions.p', 'rb'))
#keys = example.keys()
#example[keys[0]][0]

def caption_parse(caption_dict):
    cleaned_caption = {}
    keys = caption_dict.keys()
    for key in keys:
        for caption in caption_dict[key]:
            clean_caption = init_text_clean.seperate_caption(caption)
            cleaned_caption['key'] = clean_caption
    return cleaned_caption
    
def remove_nonname(string):
    names = [item.split('(')[0].strip() for item in re.split(',|and', string)]
    return names

cleaned_caption = caption_parse(allCaptions)

