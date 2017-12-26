# -*- coding: utf-8 -*- 
import os, re
import numpy as np

from sklearn.externals import joblib
from sklearn import svm

def learn(datas, labels):
    """
    データーを学習
    
    モデルを生成する
    """
    clf = svm.LinearSVC()
    clf.fit(datas, labels)
    
    return clf