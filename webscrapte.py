# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 16:18:23 2015

@author: Dao
"""

import os
import cPickle
import requests
from bs4 import BeautifulSoup


def requestSinglePage(url):
    """
    request a soup from a given url
    
    Parameters
    ----------
    url : a url string for a single page which contains
        event and photos
        
    Returns
    -------
    url: a string of url
    soup: a soup object for the given url
    
    """
    r = requests.get(url, params = {"limit" : 1000})
    soup = BeautifulSoup(r.text)
    return url, soup 
    
def getCaptionSinglePage(url, soup):
    """
    get photo caption from a soup (single page)
    each eventID corresponds to a single url
    
    Parameters
    ----------
    soup : a soup object
    eventID : a integer number to identify each page
    
    Returns
    -------
    a dictionary where the key is the url and value is all
    the photo caption on the url

    """
    soupList = soup.select('div.photocaption')
    singlePage = {url : []}
    for singleCaptionSoup in soupList:
        caption = singleCaptionSoup.text
        #SinglePageCaption(eventID = eventID, caption = caption)
        singlePage[url].append(caption)
    return singlePage

# Example usage
urlTest = u"http://www.newyorksocialdiary.com/party-pictures/2015/goodwill-and-gods-love"
url, soup = requestSinglePage(urlTest)
sampleCaption = getCaptionSinglePage(url, soup)
sampleCaption[0]


# get full url 
urls = cPickle.load(open("/Users/Dao/Desktop/GHRepo/data_incubator/urls.p", "rb"))
baseUrl = u"http://www.newyorksocialdiary.com"
fullUrls = [baseUrl+url for url in urls]


