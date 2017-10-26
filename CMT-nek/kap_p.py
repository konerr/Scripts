#!/usr/bin/python

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

# File Name : kap_p.py

# Purpose : Plot mass diffusivity(\kappa)
# as a function of time.

# Creation Date : 17-10-2017

# Last Modified :

# Created By : Rahul Koneru 

#_._._._._._._._._._._._._._._._._._._._._.

import matplotlib.pyplot as plt
import numpy as np
import os

plt.rc('text', usetex=True)
plt.rc('font', weight='bold')
plt.rc('axes', linewidth=1.4)
plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

plt.rc('xtick', labelsize=14)
plt.rc('xtick.major', size=10, pad=8)
plt.rc('xtick.minor', size=6)
plt.rc('ytick', labelsize=14)
plt.rc('ytick.major', size=10)
plt.rc('ytick.minor', size=6)


f = np.loadtxt('out.log',skiprows=2)

indx = 2 # 2=CFL 4=D_\kappa

m,c = np.polyfit(np.log(f[len(f)::-3,1]),np.log(f[len(f)-2::-3,indx]),1)

y_fit = [m * np.log(j) + c for j in f[len(f)-3::-3,1]]
plt.loglog(f[len(f)::-3,1],f[len(f)-1::-3,indx],'ob',ms=8, label=r'$N=200$')
plt.loglog(f[len(f)::-3,1],f[len(f)-2::-3,indx],'og',ms=8, label=r'$N=100$')
plt.loglog(f[len(f)::-3,1],f[len(f)-3::-3,indx],'or',ms=8, label=r'$N=50$')
plt.loglog(f[len(f)::-3,1],np.exp(y_fit),'--k', linewidth=1.8, label=r'$p^{%3.2f}$'% m)

#plt.axis('equal')
plt.xlabel(r'$\boldsymbol{p}$', fontsize=18)
plt.ylabel(r'$\boldsymbol{D_\kappa}$', fontsize=18)
plt.ylabel(r'$\boldsymbol{CFL}$', fontsize=18)
plt.legend()

plt.show()

