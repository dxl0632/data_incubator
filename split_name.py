# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:27:15 2015

@author: jing

split string into names based on "," "and"; remove long items which are not likely to be names
"""
import re
import sys
#sys.path.append('C:\Users\pc\Documents\week1\data_incubator')
import init_text_clean
import cPickle
import os
from utils import BASE_DIRECTORY
from shortName import shortName


#keys = example.keys()
#example[keys[0]][0]
def appendLastName(inputNameList):
    numWordsList=[x.strip().count(' ')+1 for x in inputNameList]
    
    currIndividual=0
    LastNames=[]
    for x  in numWordsList:
        if x>1:
            LastNames.append( inputNameList[currIndividual].split(" ")[-1])
        currIndividual+=1
    #print LastNames      
    
    currIndividual=0
    outputNameList=[]
    for x  in numWordsList:
        if x==1:
            if len(LastNames)>0:
                thisName=inputNameList[currIndividual]+" "+LastNames[0]
            else:
                thisName = inputNameList[currIndividual]
        else:
            thisName=inputNameList[currIndividual]
            del LastNames[0]
        #print thisName
        outputNameList+=[thisName]
        currIndividual+=1
    return outputNameList      



def strip_caption(caption):
    caption = re.sub(r' . ', ',', caption)
    caption = re.sub('\(.*\)', '', caption)
    caption = re.sub(r'[^a-zA-Z ,-]', ' ', caption)
    caption = re.sub(r' [a-z]+[\S]*$', ' ', caption)
    caption = re.sub(r' [a-z]+[\S]* ', ', ', caption)
    caption = re.sub(r' [a-z]+[\S]* ', ', ', caption)
    caption = re.sub(r' [a-z]+[\S]* ', ', ', caption)
    caption = re.sub(r' [a-z]+[\S]* ', ', ', caption)
    caption = re.sub(r' [a-z]+[\S]* ', ', ', caption)
    caption = re.sub(r'^[a-z]+[\S]* ', ' ', caption) 
    caption = re.sub(r'\b[A-Z]{1}\b', ' ', caption) 
    caption = re.sub(r'\bM.D.\b', ' ', caption)
    caption = re.sub(r' [A-Z]. ', ' ', caption)
    caption = re.sub(r'\b3D\b', ' ', caption)
    caption = re.sub(r'\bClose\b', ' ', caption)
    caption = re.sub(r'\bto\b', ' ', caption)
    caption = re.sub(r'\b15th\b', ' ', caption)
    caption = re.sub(r'[^a-zA-Z][A-Z][^a-zA-Z]', ' ', caption)
    caption = re.sub(r'^The,', '', caption)   
    caption = re.sub(r'\bThe\b', ',', caption)  
    caption = re.sub(r'\bNYSD\b', '', caption)
    caption = re.sub(r'\bContents\b', '', caption)
    caption = re.sub(r'\bCompany\b', '', caption)
    caption = re.sub(r'\bTeam\b', '', caption)
    caption = re.sub(r'\bthe\b', '', caption)
    caption = re.sub(r'\bChicago\b', '', caption)
    caption = re.sub(r'\bPhotographs\b', '', caption)
    caption = re.sub(r'\bBoard Member\b', '', caption)
    caption = re.sub(r'\bJBFCS Trustee\b', '', caption)
    caption = re.sub(r'\bKips Bay Boys\b', '', caption)
    caption = re.sub(r'\bFoundation\b', '', caption)
    caption = re.sub(r'\bChapter\b', '', caption)
    caption = re.sub(r'\bWashington Post\b', '', caption)
    caption = re.sub(r'\bguests\b', '', caption)
    caption = re.sub(r'\bPremiere\b', '', caption)
    caption = re.sub(r'\bYear\b', '', caption)
    caption = re.sub(r'\bCommission\b', '', caption)
    caption = re.sub(r'\bJBFCS\b', '', caption)
    caption = re.sub(r'\bPost\b', '', caption)
    caption = re.sub(r'\bClassical\b', '', caption)
    caption = re.sub(r'\bPrize-winning\b', '', caption)
    caption = re.sub(r'\bPrize\b', '', caption)
    caption = re.sub(r'\bHospital\b', '', caption)
    caption = re.sub(r'\bCommittee Co-chair\b', '', caption)
    caption = re.sub(r'\bBoard\b', '', caption)
    caption = re.sub(r'\bSteering Committee\b', '', caption)
    caption = re.sub(r'\bSurgery\b', '', caption)
    caption = re.sub(r'\bPartner Trustee\b', '', caption)
    caption = re.sub(r'\bManges Trustee\b', '', caption)
    caption = re.sub(r'\bGotshal Trustee\b', '', caption)
    caption = re.sub(r'Weil Trustee', '', caption)
    caption = re.sub(r'\bTrustee\b', '', caption)
    caption = re.sub(r'\bPortrait\b', '', caption)
    caption = re.sub(r'\bevent Commission\b', '', caption)
    caption = re.sub(r'\bMedical Center\b', '', caption)
    caption = re.sub(r'\bNew York\b', '', caption)
    caption = re.sub(r'\bCity Ballet\b', '', caption)
    caption = re.sub(r'\.', '', caption)
    caption = re.sub(r',+', ',', caption)
    caption = re.sub(r' +', ' ', caption)
    caption = caption.strip()
    return caption


def caption_clean(caption_dict):
    cleaned_caption = {}
    keys = caption_dict.keys()
    for key in keys:
        clean_caption = init_text_clean.seperate_caption(caption_dict[key])
        cleaned_caption[key] = clean_caption
    return cleaned_caption
    
def caption_parse(caption_dict):
    name_dic = {}
    keys = caption_dict.keys()
    for key in keys:
        page_list = []
        for caption in caption_dict[key]:
            if "Click" in caption or caption.startswith(u'\xa9'):
                continue
            caption = strip_caption(caption)
            name_list = []       
            for name in re.split(',',caption):
                if len(name.split())>0:
                    name_list.append(name.strip())
            name_list = shortName(name_list)
            name_list = appendLastName(name_list)
            page_list.append(name_list)
        name_dic[key]=page_list
    return name_dic    

if __name__ == "__main__":
    captionPath = os.path.join(BASE_DIRECTORY, "allCaptionsNew.p")
    allCaptions = cPickle.load(open(captionPath, 'rb'))
    cleaned_caption = caption_clean(allCaptions)
    name_dic = caption_parse(cleaned_caption)
    outputPath = os.path.join(BASE_DIRECTORY, 'name_dic2.p')
    cPickle.dump(name_dic, open(outputPath, 'wb'))       


    





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
       
def find_sth(dict):
#    caption_issue = []
#    key_issue = ''
    keys = dict.keys()
    for key in keys:
        for name_list in dict[key]:
            if 'City Ballet' in name_list:
                return key, name_list



