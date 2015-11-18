# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 16:18:40 2015

@author: pc
"""
from datetime import datetime
import cPickle
import sys
sys.path.append('"C:\Users\pc\Documents\GitHub\Web-scripping\data_incubator"')
import os
from utils import BASE_DIRECTORY

timepath = os.path.join(BASE_DIRECTORY, "event_time.p")
urlpath = os.path.join(BASE_DIRECTORY, "urls.p")
alltime = cPickle.load(open(timepath, 'rb'))
allurls = cPickle.load(open(urlpath, 'rb'))

def add_time(timels, urlls):
    url_time_dict={}
    for i, time in enumerate(timels):
        time=datetime.strptime(time.strip(), '%A, %B %d, %Y')
        key=urlls[i]
        url_time_dict[key]=time
    return url_time_dict
    
url_time=add_time(alltime, allurls)

outputpath=os.path.join(BASE_DIRECTORY, "url_time_dict.p")
cPickle.dump(url_time, open('url_time_dict.p', 'wb'))
