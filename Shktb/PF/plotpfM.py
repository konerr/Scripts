#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import scipy.io as spio
import sys
import os

plt.rc('text', usetex=True)
plt.rc('font', weight='bold')
plt.rc('axes', linewidth=1.4)
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

Ms = [1.92,1.24,1.66] 
p1 = 82700.0 
rho = 0.972177160000000 
gamma = 1.4 
us = Ms[0]*np.sqrt(gamma*p1/rho)

# Post-shock conditions (SI units) [M192,M124]
rho = [2.475479287947678,1.371897577639719,2.072513]
u = [4.024042252941134e+02,124.6810338281730,304.144,218.6620501674046]
p = [3.418928266666666e+05,134569.44,252086.14]
x_shock = 0.12
x_curt = [0.15,0.13]
curt_width = [3.5e-3,2.5e-3,1.5e-3,2e-3]
dp = 115e-6
rhop = 2500.0
phi = [0.14,0.16,0.18]
phis = np.sqrt(phi)
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
lagfile = "/pfLagrangian.dat"
dirparts = (os.getcwd(),'/2D/M145/M145_pf_small')
dirs = "".join(dirparts)

currfileparts = (dirs,'/15_14',lagfile)
currfile = "".join(currfileparts)
f1514 = np.loadtxt(currfile)

currfileparts = (dirs,'/15_16',lagfile)
currfile = "".join(currfileparts)
f1516 = np.loadtxt(currfile)

currfileparts = (dirs,'/15_18',lagfile)
currfile = "".join(currfileparts)
f1518 = np.loadtxt(currfile)

currfileparts = (dirs,'/25_14',lagfile)
currfile = "".join(currfileparts)
f2514 = np.loadtxt(currfile)

currfileparts = (dirs,'/25_16',lagfile)
currfile = "".join(currfileparts)
f2516 = np.loadtxt(currfile)

currfileparts = (dirs,'/25_18',lagfile)
currfile = "".join(currfileparts)
f2518 = np.loadtxt(currfile)

currfileparts = (dirs,'/35_14',lagfile)
currfile = "".join(currfileparts)
f3514 = np.loadtxt(currfile)

currfileparts = (dirs,'/35_16',lagfile)
currfile = "".join(currfileparts)
f3516 = np.loadtxt(currfile)

currfileparts = (dirs,'/35_18',lagfile)
currfile = "".join(currfileparts)
f3518 = np.loadtxt(currfile)

dirparts = (os.getcwd(),'/Experiments','/PVF23_M1pt45.mat')
fileM145 = "".join(dirparts)
fexpM145 = spio.loadmat(fileM145)
fexpM145 = fexpM145['PVF23_M1pt45']
del0M145 = fexpM145[0,1]-fexpM145[0,2]

del01514 = 1.0/(f1514[0,1]-f1514[0,0])
del02514 = 1.0/(f2514[0,1]-f2514[0,0])
del03514 = 1.0/(f3514[0,1]-f3514[0,0])

tau = [u[3]*del01514,u[3]*del02514,u[3]*del03514,u[3]/del0M145]

ax = plt.gca()

#plt.figure(1)
#plt.plot((f1514[:,0]-f1514[0,0])*del01514,f1514[:,2]*tsec*tau[0],'b',linewidth=1.8)
#plt.plot((f1514[:,1]-f1514[0,0])*del01514,f1514[:,2]*tsec*tau[0],'b',linewidth=1.8, label=r'$\phi_p=14\%$')
##
#plt.plot((f1516[:,0]-f1516[0,0])*del01514,f1516[:,2]*tsec*tau[0],'r',linewidth=1.8)
#plt.plot((f1516[:,1]-f1516[0,0])*del01514,f1516[:,2]*tsec*tau[0],'r',linewidth=1.8, label=r'$\phi_p=16\%$')
#
#plt.plot((f1518[:,0]-f1518[0,0])*del01514,f1518[:,2]*tsec*tau[0],'k',linewidth=1.8, label=r'$\phi_p=18\%$')
#plt.plot((f1518[:,1]-f1518[0,0])*del01514,f1518[:,2]*tsec*tau[0],'k',linewidth=1.8, label=r'$t_c=1.5mm$')
#
#plt.plot((f2514[:,0]-f2514[0,0])*del02514,f2514[:,2]*tsec*tau[1],'--b',linewidth=1.8)
#plt.plot((f2514[:,1]-f2514[0,0])*del02514,f2514[:,2]*tsec*tau[1],'--b',linewidth=1.8, label=r'$t_c=2.5mm$')
##
#plt.plot((f2516[:,0]-f2516[0,0])*del02514,f2516[:,2]*tsec*tau[1],'--r',linewidth=1.8)
#plt.plot((f2516[:,1]-f2516[0,0])*del02514,f2516[:,2]*tsec*tau[1],'--r',linewidth=1.8)
#
#plt.plot((f2518[:,0]-f2518[0,0])*del02514,f2518[:,2]*tsec*tau[1],'--k',linewidth=1.8)
#plt.plot((f2518[:,1]-f2518[0,0])*del02514,f2518[:,2]*tsec*tau[1],'--k',linewidth=1.8)
#
#plt.plot((f3514[:,0]-f3514[0,0])*del03514,f3514[:,2]*tsec*tau[2],'-.b',linewidth=1.8, label=r'$t_c=3.5mm$')
#plt.plot((f3514[:,1]-f3514[0,0])*del03514,f3514[:,2]*tsec*tau[2],'-.b',linewidth=1.8)
##                                       
#plt.plot((f3516[:,0]-f3516[0,0])*del03514,f3516[:,2]*tsec*tau[2],'-.r',linewidth=1.8)
#plt.plot((f3516[:,1]-f3516[0,0])*del03514,f3516[:,2]*tsec*tau[2],'-.r',linewidth=1.8)
#                                        
#plt.plot((f3518[:,0]-f3518[0,0])*del03514,f3518[:,2]*tsec*tau[2],'-.k',linewidth=1.8)
#plt.plot((f3518[:,1]-f3518[0,0])*del03514,f3518[:,2]*tsec*tau[2],'-.k',linewidth=1.8)
#
##plt.figure(2)
#plt.plot(fexpM145[:,1]/del0M145,fexpM145[:,0]*tsec*tau[3],'sg',linewidth=1.8)
#plt.plot(fexpM145[:,2]/del0M145,fexpM145[:,0]*tsec*tau[3],'sg',linewidth=1.8, label='Exp')

#plt.figure(2)
#ax2 = plt.gca()
plt.plot((f1514[:,1]-f1514[:,0])*del01514,f1514[:,2]*tsec*tau[0]*phis[0],'b',linewidth=1.8, label=r'$14,1.5$')
#
plt.plot((f1516[:,1]-f1516[:,0])*del01514,f1516[:,2]*tsec*tau[0]*phis[1],'r',linewidth=1.8, label=r'$16,1.5$')

plt.plot((f1518[:,1]-f1518[:,0])*del01514,f1518[:,2]*tsec*tau[0]*phis[2],'k',linewidth=1.8, label=r'$18,1.5$')

plt.plot((f2514[:,1]-f2514[:,0])*del02514,f2514[:,2]*tsec*tau[1]*phis[0],'--b',linewidth=1.8, label=r'$14,2.5$')
#
plt.plot((f2516[:,1]-f2516[:,0])*del02514,f2516[:,2]*tsec*tau[1]*phis[1],'--r',linewidth=1.8, label=r'$16,2.5$')

plt.plot((f2518[:,1]-f2518[:,0])*del02514,f2518[:,2]*tsec*tau[1]*phis[2],'--k',linewidth=1.8, label=r'$18,2.5$')

plt.plot((f3514[:,1]-f3514[:,0])*del03514,f3514[:,2]*tsec*tau[2]*phis[0],'-ob',linewidth=2.4, label=r'$14,3.5$')
#                                      
plt.plot((f3516[:,1]-f3516[:,0])*del03514,f3516[:,2]*tsec*tau[2]*phis[1],'-or',linewidth=2.4, label=r'$16,3.5$')
                                       
plt.plot((f3518[:,1]-f3518[:,0])*del03514,f3518[:,2]*tsec*tau[2]*phis[2],'-ok',linewidth=2.4, label=r'$18,3.5$')

#plt.figure(2)
phiE = np.sqrt(0.23)
plt.plot((fexpM145[:,1]-fexpM145[:,2])/del0M145,fexpM145[:,0]*tsec*tau[3]*phiE,'sg',linewidth=1.8, label='Exp')

#plt.plot(fM124_1815[:,2]*tsec/tau[3],1+1.5*(fM124_1815[:,2]*tsec/tau[3])**2,'--k',linewidth=1.8)
#plt.plot(fM124_1815[:,2]*tsec/tau[3],-1.5+3.5*fM124_1815[:,2]*tsec/tau[3],'--k',linewidth=1.8)

#ax.set_xlabel(r'$\mathbf{x(m)}$',fontsize=18)
ax.set_xlabel(r'$\mathbf{x/L}$',fontsize=18)
ax.set_xlabel(r'$\delta_x/ \delta_0$',fontsize=18)
ax.set_ylabel(r'$\mathbf{tu_2/L}$',fontsize=18)
#ax.set_ylabel(r'$\mathbf{t}(\mu \mathbf{s})$',fontsize=19)
ax.set_xlim([-0.0,18])
#ax.set_xlim([-0.001,3])
ax.set_ylim([0.0,140])
ax.tick_params(labelsize=16)
#plt.legend(loc=3,ncol=3)
ax.legend(loc='best', title=r'$\boldsymbol{\phi_p(\%)},\mathbf{t_c(mm)}$', fontsize=16)
#ax.text(14,130,r'$\mathbf{M=1.45}$', fontsize=18)
ax.text(9,130,r'$\mathbf{M=1.45}$', fontsize=18)
plt.grid()
plt.tight_layout()
#ax.set_aspect('equal')
plt.show()


