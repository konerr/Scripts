#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import sys
import os, glob
import h5py as h5

plt.rc('text', usetex=True)
#plt.rc('font', weight='bold')
plt.rc('axes', linewidth=1.4)
plt.rc('lines', linewidth=2.8)
plt.rc('xtick', labelsize=40)
plt.rc('ytick', labelsize=40)
#plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath} \boldmath"]

Ms = np.array([1.66]) 
p1 = 82700.0 
rho = 0.972177160000000 
gamma = 1.4 
us = Ms*np.sqrt(gamma*p1/rho)

# Post-shock conditions (SI units) [M192,M124]
rho = 2.072513
u = 304.144
p = 252086.14
x_shock = 0.10
x_curt = 0.13
curt_width = 2.0e-3
dp = 115e-6
phi = 0.21
mu = 1.983E-5

home = '/home/local/UFAD/rahul.koneru/post_processing/shktb'
d2d = '/2D/200_21_short'
d2d = '/2D/200_21_vp'
d2d = '/2D/200_21_short_vp'
d3d = '/3D/20_21'
sd2dparts = (os.getcwd(), d2d)
dirsd2d = "".join(sd2dparts)
file_th = '/tophat/20_21/yzavg.hdf5'
#files2d = sorted(os.listdir(dirsd2d))
files2d = glob.glob(dirsd2d+'/*yzav*')
files = sorted(files2d, key=lambda t:float(t[-15:-4]))
f_th  = h5.File(home+file_th, 'r')

plt.clf()
par = 1
#for i in files[0:len(files2d)-12:4]:
#for i in files[2:10:2]:
for i in files[::4]:
     temp = i.split('_')
     temp = temp[-1].replace('.dat','')
     if i==files[0]:
         t = 0
         grp = 'time' + '%03d' % t
     else:
         t = float(temp)*1e6
         tgrp = '%03d' % t
         t = int('%03d' % t)-50
         grp = 'time' + str(tgrp)

     x = (f_th[grp]['x'][:]-f_th[grp]['x'][1040])/curt_width
#     y = f_th[grp]['rhog']/f_th[grp]['rhog'][0]/(1.0-f_th[grp]['phip'][:])
#     y = f_th[grp]['pg']/f_th[grp]['pg'][0]
     y = f_th[grp]['ug']/f_th[grp]['ug'][0]
#     y = f_th[grp]['phip']
     f = np.loadtxt(i)
     x_nd = (f[:,0]-f[1039,0])/curt_width
#     y = abs(f[:,4]-1*f[:,-1])/np.sqrt(gamma*287.0*f[:,3])
     y = dp*(f[:,1]/(1.0-f[:,8]))*abs(f[:,4]-f[:,-1])/mu
#     y = (f[:,1]/(1.0-f[:,8]))
#     plt.plot(f[:,0],f[:,1]/rho, label='t=%d' % t )
#     plt.plot(x_nd,f[:,1]/f[0,1]/(1.0-f[:,8]), label='t = %d $\mu$s' % t )
#     plt.plot(x_nd,f[:,1]/f[0,1]/(1.0-f[:,8]), '--r', label='RBNN')
#     plt.plot(x_nd,f[:,3]/f[0,3], '--r', label='RBNN')
#     plt.plot(x,y, 'k', label='TH')
#     plt.plot(x,y, 'k', label='t = %d $\mu$s' % t)
     plt.plot(x_nd,y, label='t = %d $\mu$s' % t)

plt.ion()
fsize = 45
#plt.xlim([0.12,0.26])
#plt.xlim([-1.0,20.0])
plt.xlim([-60.0,60.0])
#plt.ylim([0.6,1.25]) # T_g
#plt.ylim([0.0,2.00]) # p_g
#plt.ylim([0.4,1.6]) # rho_g
#plt.ylim([-0.2,1.20]) # u_g
#plt.ylim([-0.2,1.2])
#plt.ylim([0.0,2.0])
#plt.yticks([0.0,0.15,0.25,0.35])
plt.xlabel(r'$\boldsymbol{x/L}$',fontsize=fsize)
plt.ylabel(r'$\boldsymbol{\phi_p}$',fontsize=fsize)
plt.ylabel(r'$\boldsymbol{u_g}$',fontsize=fsize)
plt.ylabel(r'$\boldsymbol{Ma}$',fontsize=fsize)
plt.ylabel(r'$\boldsymbol{Re_p}$',fontsize=fsize)
#plt.title(r'$\phi_p=21\%$')
plt.tight_layout()
plt.legend(loc='best', prop={'size': 17}, frameon=True)
#plt.legend(bbox_to_anchor=(0.95, 0.6), loc=2, borderaxespad=0., prop={'size': 10}, frameon=False)
#plt.show()

