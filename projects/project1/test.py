# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 18:51:43 2016

@author: ilyarudyak
"""

import matplotlib.pyplot as plt
import movie_data_helper
import numpy as np
import scipy
from scipy.misc import logsumexp
from sys import exit

x = np.array([0, 1])
prior = np.array([0.6, 0.4])
likelihood = np.array([
    [0.7, 0.98],
    [0.3, 0.02],
])
y = [0]*2 + [1]*1

log_prior = np.log(prior)
log_likelihood = np.log(likelihood)

log_posterior = np.zeros(2)

for xi in x:
    log_posterior[xi] = log_prior[xi]
    for yi in y:
        log_posterior[xi] += log_likelihood[yi, xi]
    
#log_posterior[0] = log_prior[0]
#for yi in y:
#    log_posterior[0] += log_likelihood[yi, 0]
#    
#log_posterior[1] = log_prior[1]
#for yi in y:
#    log_posterior[1] += log_likelihood[yi, 1]
   

normalizer = logsumexp(log_posterior)
log_posterior = log_posterior - normalizer
posterior = np.exp(log_posterior)
print(posterior)


















