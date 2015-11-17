# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 16:18:23 2015

@author: Dao
"""

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
    a soup for the given url
    
    """
    r = requests.get(url, params = {"limit" : 1000})
    soup = BeautifulSoup(r.text)
    return soup
    
def getCaptionSinglePage(soup, eventID):
    """
    get photo caption from a soup (single page)
    each eventID corresponds to a single url
    
    Parameters
    ----------
    soup : a soup object
    eventID : a integer number to identify each page
    
    Returns
    -------
    a list of lists, where each nested list contains 
    [eventID, photoCaption]. The length of the list is
    the total number of photo captions in given page.
    
    Example of a single item in the list: 
    [1, u" Jillian Lucas, Katie Walker, Vikram Agrawal, 
    Amanda Baron, Sarah Littman, and Sarah Boll at 
    The Children\u2019s Cancer & Blood Foundation's  
    annual Breakthrough Ball."]

    """
    soupList = soup.select('div.photocaption')
    singlePage = []
    for singleCaptionSoup in soupList:
        caption = singleCaptionSoup.text
        #SinglePageCaption(eventID = eventID, caption = caption)
        singlePage.append([eventID, caption])
    return singlePage

# Example usage
urlTest = u"http://www.newyorksocialdiary.com/party-pictures/2015/goodwill-and-gods-love"
soup = requestSinglePage(urlTest)
sampleCaption = getCaptionSinglePage(soup, 1)
sampleCaption[0]