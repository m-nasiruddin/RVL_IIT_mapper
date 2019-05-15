#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 16:56:18 2018

@author: Mohammad Nasiruddin
"""

import os
import codecs

source = codecs.open('data/input/val_small.txt', 'r', 'utf-8')
corpus = source.readlines()

for line in corpus:
    for name in os.listdir('/run/user/1000/gvfs/smb-share:server=wnas.univ-lr.fr,share=mnasirud/rvl-cdip/images/{0}'.format(os.path.split(line)[0])):
        print(name)
