#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 16:56:18 2018

@author: osboxes
"""

import os

rvlcdip_dict = {}
source = open('data/input/val.txt', 'r')
corpus = source.readlines()
for line in corpus:
    rvlcdip_dict.update({os.path.split(line)[1].split()[0].replace('+-', '/').replace('_', '/').replace('-', '/'): os.path.split(line)[1].split()[0]})

for key, value in rvlcdip_dict.items():
    print(key, value)
