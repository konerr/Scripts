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
tsec = 1e6

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
dirparts = (os.getcwd(),'/2D/M192/M192_pf_small/35_18')
dirs = "".join(dirparts)
currfileparts = (dirs,"/pfLagrangian.dat")
currfile = "".join(currfileparts)
f2D_M192_3518 = np.loadtxt(currfile)

dirparts = (os.getcwd(),'/3D/M192/35_18')
dirs = "".join(dirparts)
currfileparts = (dirs,"/pfLagrangian.dat")
currfile = "".join(currfileparts)
f3D_M192_3518 = np.loadtxt(currfile)

#dirparts = (os.getcwd(),'/1D/M145/25_14')
dirparts = (os.getcwd(),'/2D/M192/M192_pf_small/35_16')
dirs = "".join(dirparts)
currfileparts = (dirs,"/pfLagrangian.dat")
currfile = "".join(currfileparts)
f1D_M124_3518 = np.loadtxt(currfile)

#dirparts = (os.getcwd(),'/2D/M145/M145_pf_small/25_18')
#dirs = "".join(dirparts)
#currfileparts = (dirs,"/pfLagrangian.dat")
#currfile = "".join(currfileparts)
#f2D_M124_1518 = np.loadtxt(currfile)
#
#dirparts = (os.getcwd(),'/3D/M145/25_18')
#dirs = "".join(dirparts)
#currfileparts = (dirs,"/pfLagrangian.dat")
#currfile = "".join(currfileparts)
#f3D_M124_1518 = np.loadtxt(currfile)

#dirparts = (os.getcwd(),'/1D/M124/15_18')
#dirs = "".join(dirparts)
#currfileparts = (dirs,"/pfLagrangian.dat")
#currfile = "".join(currfileparts)
#f1D_M124_1518 = np.loadtxt(currfile)


ax = plt.gca()
plt.figure(1)

plt.plot((f3D_M192_3518[:,0]-f3D_M192_3518[0,0]),f3D_M192_3518[:,2]*tsec,'b',linewidth=1.8)
plt.plot((f3D_M192_3518[:,1]-f3D_M192_3518[0,0]),f3D_M192_3518[:,2]*tsec,'b',linewidth=1.8, label='3D')

plt.plot((f2D_M192_3518[:,0]-f2D_M192_3518[0,0]),f2D_M192_3518[:,2]*tsec,'r',linewidth=1.8)
plt.plot((f2D_M192_3518[:,1]-f2D_M192_3518[0,0]),f2D_M192_3518[:,2]*tsec,'r',linewidth=1.8, label='2D')

plt.plot((f1D_M124_3518[:,0]-f1D_M124_3518[0,0]),f1D_M124_3518[:,2]*tsec,'-ok',linewidth=1.8)
plt.plot((f1D_M124_3518[:,1]-f1D_M124_3518[0,0]),f1D_M124_3518[:,2]*tsec,'-ok',linewidth=1.8, label='1D')

#plt.figure(2)
#
#plt.plot((f3D_M124_1518[:,0]-x_curt[1]),f3D_M124_1518[:,2]*tsec,'b',linewidth=1.8)
#plt.plot((f3D_M124_1518[:,1]-x_curt[1]),f3D_M124_1518[:,2]*tsec,'b',linewidth=1.8)
#
#plt.plot((f2D_M124_1518[:,0]-x_curt[1]),f2D_M124_1518[:,2]*tsec,'r',linewidth=1.8)
#plt.plot((f2D_M124_1518[:,1]-x_curt[1]),f2D_M124_1518[:,2]*tsec,'r',linewidth=1.8)

#plt.plot((f1D_M124_1518[:,0]-x_curt[1]),f1D_M124_1518[:,2]*tsec,'k',linewidth=1.8)
#plt.plot((f1D_M124_1518[:,1]-x_curt[1]),f1D_M124_1518[:,2]*tsec,'k',linewidth=1.8)

#ax.set_xlabel(r'$\mathbf{x(m)}$',fontsize=18)
ax.set_xlabel(r'$\mathbf{x(m)}$',fontsize=18)
ax.set_ylabel(r'$\mathbf{t(\mu s)}$',fontsize=18)
#ax.set_ylabel(r'$\mathbf{t}(\mu \mathbf{s})$',fontsize=19)
ax.set_xlim([-0.001,0.1])
ax.set_ylim([0.0,900])
#ax.set_ylim([0.0,12])
ax.set_yticks(range(0,1000,150))
ax.tick_params(labelsize=16)
ax.set_title(r'$\mathbf{M=1.92}$, $\mathbf{\phi_p=18\%}$, $\mathbf{t_{curt}=3.5mm}$')
#ax.legend(['3D','','2D','1D'],loc='center right')
ax.legend(loc='center right')

plt.grid()
plt.tight_layout()
#ax.set_aspect('equal')
plt.show()


