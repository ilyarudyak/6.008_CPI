# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 00:48:55 2016

@author: ilyarudyak
"""

import numpy as np

prob_W_I = np.array([[1/2, 0], [0, 1/6], [0, 1/3]])
prob_W = prob_W_I.sum(axis=1)
prob_I = prob_W_I.sum(axis=0)

#print(np.outer(prob_W, prob_I))

prob_X_Y = np.array([[1/4, 1/4], [1/12, 1/12], [1/6, 1/6]])
prob_X = prob_W_I.sum(axis=1)
prob_Y = prob_W_I.sum(axis=0)

print(np.outer(prob_X, prob_Y))