# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 16:18:23 2015

@author: Dao
"""
import sys
sys.path.append("/Users/Dao/Desktop/GHRepo/data_incubator")

import os
import cPickle
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
    soupListPhoto = soup.select('div.photocaption')
    soupListFont = soup.select('div font')
    captions = []
    
    if soupListPhoto:       
        for singleCaptionSoup in soupListPhoto:
            caption = singleCaptionSoup.text
            #SinglePageCaption(eventID = eventID, caption = caption)
            captions.append(caption)
            
    if soupListFont:
        for singleCaptionSoup in soupListFont:
            caption = singleCaptionSoup.text
            #SinglePageCaption(eventID = eventID, caption = caption)
            captions.append(caption)
            
    return captions
    
    
def scrapeSinglePage(url):
    soup = requestSinglePage(url)
    return getCaptionSinglePage(soup)
    
def scrapeAllUrls(fullUrls):
    allPages = {}
    for url in fullUrls:
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
    allCaptions = scrapeAllUrls(fullUrls)
    outputPath = os.path.join(BASE_DIRECTORY, 'allCaptionsNew.p')
    cPickle.dump(allCaptions, open(outputPath, 'wb'))

