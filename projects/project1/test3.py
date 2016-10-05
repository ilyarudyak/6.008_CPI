# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 19:36:05 2016

@author: ilyarudyak
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 19:15:10 2016

@author: ilyarudyak
"""

x = [0, 1]
prior = [0.6, 0.4]
likelihood = [[0.7, 0.98],[0.3, 0.02]]
y = [0]*2 + [1]*1

posterior = [1, 1]
print(posterior)

for xi in x:
    print("prior[xi]=" + str(prior[xi]))
    posterior[xi] *= prior[xi]
    print(posterior)
    for yi in y:
        posterior[xi] *= likelihood[yi][xi]        
print(posterior)


