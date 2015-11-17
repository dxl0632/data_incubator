# -*- coding: utf-8 -*-
"""
extract contents for urls, apply filter to screen before 2014 Dec
"""

import matplotlib
import pdb
import cPickle
import requests
from bs4 import BeautifulSoup

url = "http://www.newyorksocialdiary.com/party-pictures"
#page_num = 0
urls = []
event_time = []
for page_num in xrange(26):
    manu = requests.get(url, params={"page":page_num})
    soup = BeautifulSoup(manu.text, "lxml")
    parent = soup.find('div', attrs={'class': 'view-content'})
    for x in parent.find_all('a', href=True):
        time = x.find_parent().find_parent().find_next_sibling().text
        if int(time.split()[3])<2014 or (int(time.split()[3])==2014 and time.split()[1]!='December'):
            urls.append(x['href'])
            event_time.append(time)
    page_num += 1
    #print page_num
    #print len(urls)
cPickle.dump(urls, open('urls.p', 'wb'))
cPickle.dump(event_time, open('event_time.p', 'wb'))
#pdb.set_trace()
#urls = cPickle.load(open('urls.p', 'rb'))
