#!/usr/bin/env python -*- coding: utf-8 -*-

import io, os
from itertools import chain

import numpy as np

def get_asiya_scores():
    indir = 'Asiya-outputs/'
    
    feature_data = {}
    for infile in os.listdir(indir):
        if not infile.startswith('features'):
            continue
        if infile in ['features.cp', 'features.sr', 'features.ne', 
                      'features.esa']:
            continue
        data = [[float(i) for i in line.strip().split()] 
                for line in io.open(indir+infile, 'r')]
        feature_data[infile] = data
    
    _seventy_seven = [i + j + k  for i,j,k in 
                     zip(feature_data['features.meteor'], 
                         feature_data['features.sp'], 
                         feature_data['features.ngram'])]
    seventy_seven = []
    to_remove = []

    for i,j in enumerate(_seventy_seven):
        if len(j) != 76:
            to_remove.append(i)
        else:
            seventy_seven.append(j)
    
    return seventy_seven, to_remove


#def get_asiya_scores_for_test():
'''
indir = 'Asiya-outputs/'
feature_data = {}

for infile in os.listdir(indir):
    
    if not infile.startswith('report'):
        continue
    if infile not in ['report.test.meteor', 'report.test.sp', 
                      'report.test.ngram']:
        continue
    for line in io.open(indir+infile, 'r'):
        print infile, line.split()
        break
    
    data = [[float(i) for i in line.strip().split()] 
                for line in io.open(indir+infile, 'r')]
    feature_data[infile] = data
    for line in data:
        print len(line), line
'''