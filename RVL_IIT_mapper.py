#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 18:21:15 2018

@author: Nasiruddin
"""

import codecs
import os
import xml.etree.ElementTree as eT

source = codecs.open('data/input/val_small.txt', 'r', 'utf-8')
corpus = source.readlines()
rvlcdip_dict = {}
for line in corpus:
    rvlcdip_dict.update({os.path.split(line)[1].split()[0].replace('+-', '/').replace('_', '/').replace('-', '/'):
                             os.path.split(line)[1].split()[0]})

bt_ot_dict = {}
unmatched_list = []
tree = eT.parse('data/input/iitcdip.a.a_small.xml')
root = tree.getroot()
for ltdlwocr in root.iter('LTDLWOCR'):
    for bt, ot in zip(ltdlwocr.iter('bt'), ltdlwocr.iter('ot')):
        bt_text = bt.text + '.tif'
        if bt_text in rvlcdip_dict:
            bt_ot_dict.update({rvlcdip_dict[bt_text].split('.')[0]: ot.text})

for key, value in bt_ot_dict.items():
    file = codecs.open('data/output/{0}.txt'.format(key), 'w', 'utf-8')
    file.write(value)
    file.close()
