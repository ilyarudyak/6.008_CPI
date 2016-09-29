# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 00:28:55 2016

@author: ilyarudyak
"""

import numpy as np
import matplotlib.pyplot as plt

n = np.array(range(1, 100))
plt.plot(n, 1 - (26/27)**(100 - n))
plt.xlabel('Number of rolls')
plt.ylabel('Probability of seeing face 27 at least once')