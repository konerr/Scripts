#!/usr/bin/python

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

# File Name : fit.py

# Purpose :

# Creation Date : 31-05-2018

# Last Modified :

# Created By : Rahul Koneru 

#_._._._._._._._._._._._._._._._._._._._._.

import matplotlib.pyplot as plt
import numpy as np

sampl = 900
M = np.linspace(0.6, 0.96, num=sampl)
Cd = np.linspace(1e-6, 1.0, num=sampl)

f=np.polyfit(M,np.log(Cd),1)
print(f[0],np.exp(f[1]))

Cd_fit = np.exp(f[1])*np.exp(f[0]*M)
Cd_fit = 7.819E-09*np.exp(19.44*M)

plt.plot(M, Cd_fit)

