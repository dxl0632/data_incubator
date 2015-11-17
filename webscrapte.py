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
<<<<<<< HEAD
    try:
        r = requests.get(url)
    except ConnectionError as e:
        r = 'No response'
    
    if not isinstance(r, str):
        soup = BeautifulSoup(r.text)
        
=======
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
>>>>>>> d8dc7d56487a35948da26858fe2270f09d701431
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
    soupList = soup.select('div.photocaption')
    if soupList:
        captions = []
        for singleCaptionSoup in soupList:
            caption = singleCaptionSoup.text
            #SinglePageCaption(eventID = eventID, caption = caption)
            captions.append(caption)
        return captions
    else:
        return []

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
    urls = cPickle.load(open(urlPath, "rb"))
    baseUrl = u"http://www.newyorksocialdiary.com"
    fullUrls = [baseUrl+url for url in urls]
    allCaptions = scrapeAllUrls(fullUrls)
    outputPath = os.path.join(BASE_DIRECTORY, 'allCaptions.p')
    cPickle.dump(allCaptions, open(outputPath, 'wb'))

