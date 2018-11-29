#!/usr/bin/python

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

# File Name : plothist.py

# Purpose : Plot histograms of particle 
#	    number density. 

# Creation Date : 22-01-2018

# Last Modified :

# Created By : Rahul Koneru 

#_._._._._._._._._._._._._._._._._._._._._.

import matplotlib.pyplot as plt
import numpy as np
import scipy.io as spio
import os
import time

start_time = time.time()

plt.rc('text', usetex=True)
plt.rc('font', weight='bold')
plt.rc('axes', linewidth=1.4)
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

basedir = os.getcwd()
#av2D = '/shktb.yzavg_0.00000E+00.dat'
#av3D = '/shktb.yzavg_0.00000E+00.dat'
av2D = '/shktb_3.00169E-04.plag'
av2Ds = '/shktb_3.00120E-04.plag'
av3D = '/shktb_3.00127E-04.plag'
#av2D = '/shktb.yzavg_4.00219E-04.dat'
#av3D = '/shktb.yzavg_4.00224E-04.dat'
#av2D = '/shktb.yzavg_4.50275E-04.dat'
#av3D = '/shktb.yzavg_4.50284E-04.dat'
#av2D = '/shktb.yzavg_4.75294E-04.dat'
#av3D = '/shktb.yzavg_4.75297E-04.dat'
ext = '.npz'
#av1Dparts = (basedir, '/1D/200_21', av1D, ext)
av2Dparts = (basedir, '/2D/200_21', av2D, ext)
av2Dsparts = (basedir, '/2D/200_21_short', av2Ds, ext)
av3Dparts = (basedir, '/3D/20_21', av3D, ext)

#fL1D = "".join(fL1Dparts)
av2D = "".join(av2Dparts)
av2Ds = "".join(av2Dsparts)
av3D = "".join(av3Dparts)
files = [av2D, av3D, av2Ds]

f2D  = np.load(files[0])
f2Ds = np.load(files[2])
f3D  = np.load(files[1])

x0 = 0.13
dx = 125e-6

xmin2D = min(i for i in f2D['x'][:] if i>0)
xmin3D = min(i for i in f3D['x'][:] if i>0)
xmax2D = max(f2D['x'][:])
xmax3D = max(f3D['x'][:])
xmin = min(xmin2D,xmin3D)
xmax = max(xmax2D,xmax3D)
# Range can only take int, xint is a list
xint = range(int(xmin*1e6),int((xmax+dx)*1e6),int(dx*1e6))
# Convert xint to floats
xhist = [float(i)*1e-6 for i in xint]
# Shifting origin
xhist = np.array(xhist)-x0
# Plotting shit
par =8 
if par == 2:
    scale = 1e-6
    label = 'P(MPa)'
    xL = -0.1
    xR = 0.22
    yB = 0.08
    yT = 0.45
elif par == 8:
     scale = 1
     label = r'$N_p$'
     xL = -0.01
     xR = 0.04
     yB = -0.001
     yT = 0.06

plt.ion()
plt.figure(1)
plt.tight_layout()
ax = plt.gca()
# fc=(R,G,B,A)
arr, bins, patches =plt.hist(f2D['x'][:]-x0, bins=xhist, color='green',normed=True, edgecolor='black', linewidth=1.2)
plt.hist(f3D['x'][:]-x0, bins=xhist, fc=(1,0,0,0.5),normed=True, edgecolor='black', linewidth=1.2)
plt.hist(f2Ds['x'][:]-x0, bins=xhist, fc=(0,0,1,0.5),normed=True, edgecolor='black', linewidth=1.2)

plt.xlim(0, xmax-x0+2*dx)
#plt.ylim(yB, yT)
plt.xlabel('x(m)',fontsize=16)
plt.ylabel(label,fontsize=16)
#ax.set_xticks(range(0,951,150))
ax.tick_params(labelsize=16)
ax.legend(loc='upper right')
print('%s seconds' % (time.time() - start_time))
