# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:37:21 2020

@author: psiit
"""

import matplotlib.pyplot as plt
import numpy as np

s = np.linspace(0.1, 10, 100)*1j

Hs = 1/(s*(s+1))

plt.figure()
plt.subplot(211)
plt.plot(abs(s), abs(Hs))
plt.yscale('log')
plt.xscale('log')
plt.grid(True)
plt.subplot(212)
plt.plot(abs(s), np.angle(Hs))
#plt.yscale('log')
plt.xscale('log')
plt.grid(True)
plt.show()