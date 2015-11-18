# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 16:18:23 2015

@author: Dao
"""
import sys
sys.path.append("/Users/Dao/Desktop/GHRepo/data_incubator")
import os
import cPickle
from multiprocessing import Pool
from itertools import chain

import requests
from requests.exceptions import  ConnectionError
from bs4 import BeautifulSoup

from utils import BASE_DIRECTORY

def requestSinglePage(url):
    """
    request a soup from a given url
    
    Parameters
    ----------
    url : a url string for a single page which contains
        event and photos
        
    Returns
    -------
    soup: a soup object for the given url
    
    """
    try:
        r = requests.get(url)
    except ConnectionError as e:
        r = 'No response'
    
    if not isinstance(r, str):
        soup = BeautifulSoup(r.text)
        return soup 
        

     
def getTagList(soup):
    tagLists = []
    tagLists.append(soup.select('div.photocaption'))
    tagLists.append(soup.select('div font'))
    tagLists.append(soup.select('td.photocaption'))
    return tagLists
    
def tagToCaption(tagList):
    captions = []
    for tag in tagList:
        caption = tag.text
        if caption:
            captions.append(caption)
    return captions
    
def getCaptionSinglePage(soup):
    """
    get photo caption from a soup (single page)
    each eventID corresponds to a single url
    
    Parameters
    ----------
    soup : a soup object
    eventID : a integer number to identify each page
    
    Returns
    -------
    a list of all photo captions for the given url

    """
    
    tagLists = getTagList(soup)
    captions = []
    for tagList in tagLists:
        if tagList:
            caption = tagToCaption(tagList)
            captions.append(caption)      
    return list(chain(*captions))
    
    
def scrapeSinglePage(url):
    soup = requestSinglePage(url)
    if soup is not None:
        return getCaptionSinglePage(soup)
    
def scrapeAllUrls(fullUrls, noisy = False):
    allPages = {}
    for url in fullUrls:
        if noisy: 
            print url
        allPages[url] = scrapeSinglePage(url)
    return allPages
    
 

if __name__ == "__main__":
    # get full url 
    urlPath = os.path.join(BASE_DIRECTORY, "urls.p")
    #eventPath = os.path.join(BASE_DIRECTORY, "event_time.p")
    
    urls = cPickle.load(open(urlPath, "rb"))
    #eventTime = cPickle.load(open(eventPath, "rb"))
    
    baseUrl = u"http://www.newyorksocialdiary.com"
    fullUrls = [baseUrl+url for url in urls]
    
    #p = Pool(20) # have 20 processes
    #allCaptions = p.map(scrapeAllUrls, fullUrls)
    allCaptions = scrapeAllUrls(fullUrls, noisy=True)
    # deal with NoneType in list
    for key in allCaptions:
        if allCaptions[key] is None:
            allCaptions[key] = []
            
    outputPath = os.path.join(BASE_DIRECTORY, 'allCaptionsNew.p')
    cPickle.dump(allCaptions, open(outputPath, 'wb'))

