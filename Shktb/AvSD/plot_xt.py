#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import sys
import os, glob
import h5py as h5

plt.rc('text', usetex=True)
#plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath} \usepackage{sfmath} \boldmath "]
plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath} \boldmath "]
#plt.rc('font', weight='bold')
plt.rc('axes', linewidth=1.6)
plt.rc('lines', linewidth=2.8)
plt.rcParams['lines.markersize'] = 12
plt.rc('xtick', labelsize=40)
plt.rc('ytick', labelsize=40)
#plt.rc('font',**{'family':'sans-serif', 'weight':'bold'})
plt.rcParams["figure.figsize"] = [9.8,12.8]
plt.rcParams["xtick.direction"] = 'in'
plt.rcParams["ytick.direction"] = 'in'
plt.rcParams["xtick.minor.visible"] = True
plt.rcParams["ytick.minor.visible"] = True
#plt.rcParams["xtick.major.top"] = True
#plt.rcParams["ytick.major.right"] = True
plt.rcParams["xtick.minor.top"] = True
plt.rcParams["ytick.minor.right"] = True
plt.rcParams["xtick.top"] = True
plt.rcParams["ytick.right"] = True
plt.rcParams["xtick.major.size"] = 10
plt.rcParams["ytick.major.size"] = 10
plt.rcParams["xtick.minor.size"] = 5
plt.rcParams["ytick.minor.size"] = 5
plt.clf()

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
#home = os.getcwd()
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
len_f_th = len(list(f_th.items()))
t_xt = np.zeros(len_f_th)
z_xt = np.zeros((len(t_xt),len(f_th['time000']['x'])))
z2_xt = np.zeros((len(t_xt),len(f_th['time000']['x'])))

plt.clf()
par = 1
j = 0
#for i in files[0:len(files2d)-12:4]:
#for i in files[2:10:2]:
#for i in files[::4]:
#for i in files[:]:
for indx, i in enumerate(np.arange(0,860,step=25)):
#     temp = i.split('_')
#     temp = temp[-1].replace('.dat','')
#     if i==files[0]:
#         t = 0
#         grp = 'time' + '%03d' % t
#     else:
#         t = float(temp)*1e6
#         tgrp = '%03d' % t
#         t = int('%03d' % t)-50
#         grp = 'time' + str(tgrp)

     tgrp = '%03d' % i
     grp = 'time' + str(tgrp)
     x_xt = (f_th[grp]['x'][:]-f_th[grp]['x'][1040])/curt_width
     t_xt[indx] = f_th[grp].attrs['time']*1E-6*us/curt_width
     z_xt[indx,:] = f_th[grp]['rhog'][:]
     z2_xt[indx,:] = f_th[grp]['phip'][:]
#     x = (f_th[grp]['x'][:]-f_th[grp]['x'][1040])/curt_width
#     y = f_th[grp]['rhog']/f_th[grp]['rhog'][0]/(1.0-f_th[grp]['phip'][:])
#     y = f_th[grp]['pg']/f_th[grp]['pg'][0]
#     y = f_th[grp]['ug']/f_th[grp]['ug'][0]
#     y = f_th[grp]['phip']

#     f = np.loadtxt(i)
#     x_nd = (f[:,0]-f[1039,0])/curt_width
#     y = abs(f[:,4]-1*f[:,-1])/np.sqrt(gamma*287.0*f[:,3])
#     y = dp*(f[:,1]/(1.0-f[:,8]))*abs(f[:,4]-f[:,-1])/mu
#     y = (f[:,1]/(1.0-f[:,8]))
     j = j+1

#f_th.close()
#plt.ion()
fsize = 45
xmin = -65 #min(x_xt)
xmax = 110 #max(x_xt)
ymin = min(t_xt)
ymax = 250 #max(t_xt)
#plt.contourf(x_xt,t_xt, z_xt, 30)
#contours = plt.contour(x_xt,t_xt, z_xt, 3, colors='red')
#plt.clabel(contours, inline=True, fontsize=8)
plt.imshow(z_xt, extent=[xmin, xmax, ymin, ymax], origin='lower',
        cmap='gist_gray',
        alpha=1.0, interpolation='gaussian')
#plt.imshow(z2_xt, extent=[xmin, xmax, ymin, ymax], origin='lower', cmap='binary',
#        alpha=0.3, interpolation='gaussian')
#plt.yticks([0.0,0.15,0.25,0.35])
plt.xlabel(r'$\mathbf{x/L}$',fontsize=fsize)
plt.ylabel(r'$\boldsymbol{tu_s/L}$',fontsize=fsize)
#plt.title(r'$\phi_p=21\%$')
#cbar = plt.colorbar()
#cbar.ax.set_ylabel(r'$\rho_g$', fontsize=fsize, rotation=0, labelpad=30)
#cbar.ax.text(1.3, 0.5, r'$\rho_g$', fontsize=fsize, rotation=90)
plt.axis(aspect='image')
plt.tight_layout()
#plt.legend(bbox_to_anchor=(0.95, 0.6), loc=2, borderaxespad=0., prop={'size': 10}, frameon=False)
#plt.show()

