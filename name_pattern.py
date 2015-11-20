# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 16:38:29 2015

@author: pc
"""
global name_reg
name_reg = re.compile(r'(([A-Z][a-z]+ )+([a-z]+ )?[A-Z][a-z]+)')
def strip_name(string):
    global name_reg
    m = name_reg.match(string)
    if m is not None:
        return m.groups()[0]
    pass

def split_name(string):  
    '''
    input: sub-captions
    output: list of names
    
    1. remove () and split by ",", "with"
    '''
    names_clean = []
    names = [item.split('(')[0].strip() for item in re.split(',|and|with', string)]
    for name in names:
        names_clean.append(strip_name(name))
    return names_clean
