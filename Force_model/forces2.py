#!/bin/bash

import numpy as np
import h5py as h5
import matplotlib.pyplot as plt
#import matplotlib.animation as animation

plt.rc('text', usetex=True)
plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath} \usepackage{sfmath} \boldmath "]
#plt.rc('font', weight='bold')
plt.rc('axes', linewidth=1.6)
#plt.rc('lines', linewidth=2.0)
#plt.rcParams['lines.markersize'] = 12
plt.rc('xtick', labelsize=40)
plt.rc('ytick', labelsize=40)

Ms = 3
dp = 100.0E-06
rho2 = 4.646995959227003
u2 = 7.625292805549852E+02
us = 1.029414528749230E+03
A_proj = 0.25*np.pi*dp**2

f_proj = 0.5*rho2*u2*u2*A_proj
tau = dp/us
#phi = 10
clrs = ['^k','^r','^g','^b']
k = 3
hf = h5.File('Mesoscale/NoFluc/phi25_new_intrp1/forces.hdf5','r')
#hf = h5.File('Mesoscale/NoFluc/tests/phi10_cdinv/forces.hdf5','r')
#hf = h5.File('Mesoscale/NoFluc/phi15_new/forces.hdf5','r')
#hf = h5.File('Mesoscale/NoFluc/phi10/forces.hdf5','r')
#hf2 = h5.File('forces2.hdf5','a')

ngrps = len(list(hf.keys()))
grp0 = list(hf.keys())[0]
ndset = 3*len(list(hf[grp0].keys()))
npcls = hf.attrs['npcls']
dp = hf.attrs['dp']
phi = hf.attrs['phi']*100 # In %
print(ngrps,npcls,ndset)

times = np.zeros(ngrps)
f_all = np.zeros((npcls,ndset,ngrps))
for indx, grp in enumerate(list(hf.keys())):
#    print(grp,indx)
    f_all[0:npcls,0:ndset,indx] = np.hstack((hf[grp]['xyz'], # [0:2]
                                             hf[grp]['Fqs'], # [3:5]
                                             hf[grp]['Fpg'], # [6:8]
                                             hf[grp]['Fiu'], # [9:11]
                                             hf[grp]['Fvu'], # [12:14]
                                             hf[grp]['Ftot'], # [15:17]
                                             ))
    times[indx] = hf[grp].attrs['time'] 

hf.close()
f2_all = np.transpose(f_all)

#plt.clf()
plt.ion()
cmap = plt.get_cmap('Dark2')
#cmap = plt.get_cmap('hsv')
colors = cmap(np.linspace(0, 1.0, npcls))
#colors = cmap(np.linspace(0, 1.0, ngrps+1))

#fig, ax = plt.subplots()
#x = times[0]/tau
#y = (f2_all[0,6,0]*0+f2_all[0,9,0])/f_proj
#line, = ax.plot(x,y)
#

#for i in range(0,ngrps+1):
#    plt.plot(times/tau, (f_all[i,6,:]*0+f_all[i,9,:])/f_proj, color=colors[i])

#plt.figure()
#plt.cla()
for i in range(0,npcls-150,1):
    f_nd = (f2_all[:,6,i]*1+1*f2_all[:,9,i]-1*f2_all[:,3,i])/f_proj
    x_nd = f2_all[:,0,i]/dp
#    plt.plot(times/tau,(f2_all[:,6,i]*1+0*f2_all[:,9,i])/f_proj, color=colors[i])
#    plt.plot(times/tau,(f2_all[:,6,i]*0+1*f2_all[:,9,i])/f_proj, label='Pcl %d' %i)
    plt.plot(x_nd[0], np.max(f_nd), '.k')
#    plt.plot(i, np.trapz((f2_all[:,6,i]*1+1*f2_all[:,9,i]-0*f2_all[:,3,i])/f_proj, times/tau), '^b',
#        markersize=4)
#    plt.semilogx(i+1,
#            np.trapz((f2_all[:,6,i]*1+1*f2_all[:,9,i]-1*f2_all[:,3,i])/f_proj,
#                times/tau), clrs[k], markersize=8)
#    plt.plot(i, np.trapz(times,
#        (f2_all[:,6,i]*1+1*f2_all[:,9,i]-0*f2_all[:,3,i])), '^r',
#        markersize=4)
#    plt.savefig('pcl%03d.png' %i)

fsize = 40
plt.xlabel(r'$t/ \tau$', fontsize=fsize)
plt.ylabel(r'$C_{D,tot}$', fontsize=fsize)
#plt.xlabel(r'$\mathit{i_{pcl}}$', fontsize=fsize)
#plt.ylabel('Impulse', fontsize=fsize)
#plt.ylim([-2.5, 35])
#plt.xlim([0.7079812002696424, 100])
#plt.xlim([-0.75, 15])
plt.xlim([9.75, 22])
plt.ylim([-5.0, 15])
#plt.ylim([-0.1, 1.5])
plt.title(r'$ \boldsymbol{\phi_p= %d\%%} $ ' % phi, fontsize=fsize)
plt.tight_layout()
plt.legend()
#plt.show()
