# -*- coding: utf-8 -*-
"""
extract contents for urls, apply filter to screen before 2014 Dec
"""

import matplotlib
#import seaborn as sns
import requests
from bs4 import BeautifulSoup

url = "http://www.newyorksocialdiary.com/party-pictures"
manu = requests.get(url, params={"page":3})
#print manu.url
#print manu.text[:1000]
soup = BeautifulSoup(manu.text)
parent = BeautifulSoup(soup.find_all('div', attrs={'class': 'view-content'}).text)

url = []
for a in parent.select('div.view-content a', href=True, ):
    print "Found the URL:", a['href']

