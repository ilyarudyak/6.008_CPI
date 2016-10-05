# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 19:15:10 2016

@author: ilyarudyak
"""
import numpy as np

x = np.array([0, 1])
prior = np.array([0.6, 0.4])
likelihood = np.array([
    [0.7, 0.98],
    [0.3, 0.02],
])
y = [0]*2 + [1]*1

posterior = [1, 1]
print(posterior)

for xi in x:
    print("prior[xi]=" + str(prior[xi]))
    posterior[xi] = posterior[xi] * prior[xi]
    print(posterior)
    for yi in y:
        posterior[xi] = posterior[xi] * likelihood[yi, xi]        
print(posterior)

posterior = np.array(posterior)

normalizer = posterior.sum()
print(normalizer)

posterior = posterior / normalizer
print(posterior)
