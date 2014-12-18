#!/usr/bin/env python -*- coding: utf-8 -*-

import math

import numpy as np

import cPickle as pickle

from sklearn.linear_model import LinearRegression, BayesianRidge, ARDRegression
from sklearn.linear_model import ElasticNet, LogisticRegression, RandomizedLogisticRegression
from sklearn.linear_model import PassiveAggressiveRegressor, RANSACRegressor
from sklearn.isotonic import IsotonicRegression
from sklearn import ensemble
from sklearn.svm import SVR
from sklearn.gaussian_process import GaussianProcess
from sklearn.tree import DecisionTreeRegressor


x = np.loadtxt('x.asiya.train')
y = np.loadtxt('y.asiya.train')

regressors = {'lr':LinearRegression(),
'br':BayesianRidge(compute_score=True),
'enr':ElasticNet(),
'par':PassiveAggressiveRegressor(),
'ransac':RANSACRegressor(),
'lgr':LogisticRegression(),
'svr_lin':SVR(kernel='linear', C=1e3),
'svr_poly':SVR(kernel='poly', C=1e3, degree=2),
'svr_rbf':SVR(kernel='rbf', C=1e3, gamma=0.1)}

def build_regressors(num):
    rgs = regressors[num]
    rgs.fit(x, y)
    with open(num+'.pk', 'wb') as fid:
        pickle.dump(rgs, fid)


trained_regressors = {pickle.load(open(i+'.pk', 'rb')) for i in regressors
                      if i not in ['svr_poly', 'svr_lin']}


    
def main(num):
    build_regressors(num)

if __name__ == '__main__':
  import sys
  main(*sys.argv[1:])

