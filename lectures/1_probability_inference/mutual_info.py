# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 00:41:40 2016

@author: ilyarudyak
"""

import numpy as np
import math

joint_prob_XY = np.array([[0.10, 0.09, 0.11], [0.08, 0.07, 0.07], [0.18, 0.13, 0.17]])

prob_X = joint_prob_XY.sum(axis=1)
prob_Y = joint_prob_XY.sum(axis=0)

joint_prob_XY_indep = np.outer(prob_X, prob_Y)

mutual_info_XY = 0
for i in range(3):
    for j in range(3):
        ratio = joint_prob_XY[i, j] / joint_prob_XY_indep[i, j]
        mutual_info_XY += joint_prob_XY[i, j] * math.log(ratio, 2)
        
        