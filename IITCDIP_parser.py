#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 15:07:43 2018

@author: Nasiruddin
"""

import xml.etree.ElementTree as eT

bt_ot_dict = {}
tree = eT.parse('data/input/iitcdip.a.a_small.xml')
root = tree.getroot()
for ltdlwocr in root.iter('LTDLWOCR'):
    for bt, ot in zip(ltdlwocr.iter('bt'), ltdlwocr.iter('ot')):
        bt_ot_dict.update({bt.text+'.tif': ot.text})

#for key, value in bt_ot_dict.items():
#    print('KEY: ', key, value)
if '2040977284.tif' in bt_ot_dict:
    print(bt_ot_dict['2040977284.tif'])
