#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 16:56:18 2018

@author: osboxes
"""

import codecs
import os

rvlcdip_list = []
source = codecs.open('data/input/val.txt', 'r', 'utf-8')
corpus = source.readlines()
for line in corpus:
    rvlcdip_list.extend([line.split()[0], line.split()[1], os.path.split(line)[1].split()[0].replace('+-', '/').replace('_', '/')
                        .replace('-', '/'), os.path.split(line)[1].split()[0]])

for item in range(0, len(rvlcdip_list), 4):
    print(rvlcdip_list[item + 1])
