#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 18:21:15 2018

@author: Nasiruddin
"""

import xml.etree.ElementTree as et
import re

source = open('data/input/val.txt', 'r')
corpus = source.readlines()
rvlcdip_list = []
for line in corpus:
    rvlcdip_list.append(re.findall(r'[+_a-z0-9\.-]*.tif', line))

bt_ot_dict = {}
tree = et.parse('data/input/iitcdip.a.a.xml')
root = tree.getroot()
for ltdlwocr in root.iter('LTDLWOCR'):
    for bt, ot in zip(ltdlwocr.iter('bt'), ltdlwocr.iter('ot')):
        new_bt = bt.text.split('/')[0]
        if new_bt in str(rvlcdip_list):
            bt_ot_dict.update({new_bt : ot.text})

for key, value in bt_ot_dict.items():
    print(key, value)
