# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 12:34:12 2015

@author: Dao
"""
import os 
import cPickle
import sys
sys.path.append("/Users/Dao/Desktop/GHRepo/data_incubator")

from utils import BASE_DIRECTORY
from nameparser import HumanName
from nameparser.config import CONSTANTS

# read all captions
captionPath = os.path.join(BASE_DIRECTORY, 'allCaptions.p')
allCaptions = cPickle.load(open(captionPath, 'rb'))
keys = allCaptions.keys()
captionString = allCaptions[keys[0]][0]

# customize title
# not working
#CONSTANTS.titles.remove("center")

# parse a string and determine name
#name = "Diane von Furstenberg" 
#rawName = "Lincoln Center President Jed Bernstein"
#rawName = "Dr. Daoying Lin Jr."
#name = "President Jed Bernstein"
#name = "Mayor Bloomberg whatever"


def parsingName(rawName):
    humanName = HumanName(rawName)
    first = humanName.first
    middle = humanName.middle
    last = humanName.last
    suffix = humanName.suffix
    name = " ".join([first, middle, last]).strip()
    nameNoExtraSpace = " ".join(name.split())
    return nameNoExtraSpace
    
    
  