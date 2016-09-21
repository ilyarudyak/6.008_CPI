# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 23:40:35 2016

@author: ilyarudyak
"""

import comp_prob_inference

prob_space = {'sunny': 1/2, 'rainy': 1/6, 'snowy': 1/3}
random_outcome = comp_prob_inference.sample_from_finite_probability_space(prob_space)
W = random_outcome
if random_outcome == 'sunny':
    I = 1
else:
    I = 0
print(I)