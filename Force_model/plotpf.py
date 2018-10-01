#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import sys
import os

plt.rc('text', usetex=True)
plt.rc('font', weight='bold')
plt.rc('axes', linewidth=1.4)
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

Ms = [1.92,1.24] 
p1 = 82700.0 
rho = 0.972177160000000 
gamma = 1.4 
us = Ms[0]*np.sqrt(gamma*p1/rho)

# Post-shock conditions (SI units) [M192,M124]
rho = [2.475479287947678,1.371897577639719]
u = [4.024042252941134e+02,124.6810338281730]
p = [3.418928266666666e+05,134569.44]
x_shock = 0.12
x_curt = [0.15,0.13]
curt_width = [3.5e-3,2.5e-3,1.5e-3]
dp = 115e-6
rhop = 2500.0
phi = 0.18
tsec = 1e0

# Compute P_wall Theofanous JFM 2016
#compPwall()
a = 1.0
b = [-(2+0.5*gamma*(gamma+1)*Ms[0]**2),-(2+0.5*gamma*(gamma+1)*Ms[1]**2)]
c = [1-0.5*gamma*(gamma-1)*Ms[0]**2,1-0.5*gamma*(gamma-1)*Ms[1]**2]
eta = [np.roots([a,b[0],c[0]]),np.roots([a,b[1],c[1]])]
eta = [max(eta[0]),max(eta[1])]
pwall = [eta[0]*p[0],eta[1]*p[1]]

# Time scale based on post-shock velocity 
# Ling et. al Phys of Fluids 2012
tau = [curt_width[0]/u[0],curt_width[0]/u[1],curt_width[1]/u[1],curt_width[2]/u[1]]
# Theofanous JFM 2016
und = [np.sqrt( (p1/rhop)*( (pwall[0]/p1)-1 ) ), np.sqrt( (p1/rhop)*( (pwall[1]/p1)-1 ) )]
tau = [curt_width[0]/und[0],curt_width[0]/und[1],curt_width[1]/und[1],curt_width[2]/und[1]]

#files2d = sorted(os.listdir(dirsd2d))
dirparts = (os.getcwd(),'/3D_SD')
dirs = "".join(dirparts)

currfileparts = (dirs,"/pfLagrangian.dat")
currfile = "".join(currfileparts)

f = np.loadtxt(currfile)

dirparts = (os.getcwd(),'/pfEL_files','/18_35')
dirs = "".join(dirparts)

currfileparts = (dirs,"/pfLagrangian.dat")
currfile = "".join(currfileparts)

fM124 = np.loadtxt(currfile)

dirparts = (os.getcwd(),'/pfEL_files','/18_25')
dirs = "".join(dirparts)

currfileparts = (dirs,"/pfLagrangian.dat")
currfile = "".join(currfileparts)

fM124_1825 = np.loadtxt(currfile)

dirparts = (os.getcwd(),'/pfEL_files','/18_15')
dirs = "".join(dirparts)

currfileparts = (dirs,"/pfLagrangian.dat")
currfile = "".join(currfileparts)

fM124_1815 = np.loadtxt(currfile)


ax = plt.gca()
#plt.plot((f[:,0]-x_curt[0])/curt_width,f[:,2]*tsec/tau[0],'b',linewidth=1.8)
#plt.plot((f[:,1]-x_curt[0])/curt_width,f[:,2]*tsec/tau[0],'b',linewidth=1.8)
#
#plt.plot((fM124[:,0]-x_curt[1])/curt_width,fM124[:,2]*tsec/tau[1],'b',linewidth=1.8)
#plt.plot((fM124[:,1]-x_curt[1])/curt_width,fM124[:,2]*tsec/tau[1],'b',linewidth=1.8)

#plt.plot((f[:,0]-x_curt[0]),f[:,2]*tsec,'b',linewidth=1.8)
#plt.plot((f[:,1]-x_curt[0]),f[:,2]*tsec,'b',linewidth=1.8)
#
#plt.plot((fM124[:,0]-x_curt[1]),fM124[:,2]*tsec,'r',linewidth=1.8)
#plt.plot((fM124[:,1]-x_curt[1]),fM124[:,2]*tsec,'r',linewidth=1.8)

plt.plot(f[:,2]*tsec/tau[0],(f[:,1]-f[:,0])/curt_width[0],'b',linewidth=1.8)

plt.plot(fM124[:,2]*tsec/tau[1],(fM124[:,1]-fM124[:,0])/curt_width[0],'r',linewidth=1.8)

plt.plot(fM124_1825[:,2]*tsec/tau[2],(fM124_1825[:,1]-fM124_1825[:,0])/curt_width[1],'k',linewidth=1.8)

plt.plot(fM124_1815[:,2]*tsec/tau[3],(fM124_1815[:,1]-fM124_1825[:,0])/curt_width[2],'g',linewidth=1.8)

#plt.plot(fM124_1815[:,2]*tsec/tau[3],1+1.5*(fM124_1815[:,2]*tsec/tau[3])**2,'--k',linewidth=1.8)
plt.plot(fM124_1815[:,2]*tsec/tau[3],-1.5+3.5*fM124_1815[:,2]*tsec/tau[3],'--k',linewidth=1.8)

#ax.set_xlabel(r'$\mathbf{x(m)}$',fontsize=18)
ax.set_ylabel(r'$\mathbf{x^*}$',fontsize=18)
ax.set_xlabel(r'$\mathbf{t^*}$',fontsize=18)
#ax.set_ylabel(r'$\mathbf{t}(\mu \mathbf{s})$',fontsize=19)
#ax.set_xlim([-0.001,30])
ax.set_xlim([-0.001,3])
ax.set_ylim([0.0,12])
ax.tick_params(labelsize=16)
ax.legend(['3D'],loc='center right')

plt.grid()
plt.tight_layout()
#ax.set_aspect('equal')
plt.show()


