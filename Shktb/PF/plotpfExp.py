#!/usr/bin/python

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

# File Name : plotpfExp.py

# Purpose : Plot shktb profiles from 
#           experimental data

# Creation Date : 24-10-2017

# Last Modified :

# Created By : Rahul Koneru 

#_._._._._._._._._._._._._._._._._._._._._.

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

Ms = np.array([1.92, 1.66, 1.45]) 
p1 = 82700.0 
rho = 0.972177160000000 
gamma = 1.4 
us = Ms*np.sqrt(gamma*p1/rho)

# Post-shock conditions (SI units) [M192,M166,M145]
rho = np.array([2.475479287947678, 2.072513, 1.726718038481557])
u = np.array([4.024042252941134e+02,304.144,218.6620501674046])
p = np.array([3.418928266666666e+05,252086.14,189072.8750])
x_shock = 0.10
x_curt = 0.13
curt_width = 2e-3
dp = 115e-6
rhop = 2500.0
phi = 0.18
tsec = 1e0

syms = ['r','b','g','--r','--b','--g']

# Compute P_wall Theofanous JFM 2016
#def compPwall():
#    global pwall
a = np.ones(3)
b = -(2+0.5*gamma*(gamma+1)*Ms**2)
c = 1-0.5*gamma*(gamma-1)*Ms**2
eta = np.roots([a[0],b[0],c[0]])
#print (eta[0],eta[1])
eta = max(eta)
pwall = eta*p

#if any(pwall/p1) <= 1:
#	print ('Pwall is too small, check the expression...', pwall/p1)
#	sys.exit(1)

def taus(tindx):
#    compPwall()
    global tau
# Time scale based on post-shock velocity 
# Ling et. al Phys of Fluids 2012
    if tindx == 1:
        tau = curt_width/u 
    elif tindx == 2:
# Theofanous JFM 2016
        und = np.sqrt( (p1/rhop)*((pwall/p1)-1) )
        tau = curt_width/und

def pf_scaledplot(indx):
    plt.figure(1)
    plt.plot((fexpM192[:,1])/del0M192,fexpM192[:,0]*tsec/tau[0],'k', linewidth=1.8, label=r'$M=1.92$')
    plt.plot((fexpM192[:,2])/del0M192,fexpM192[:,0]*tsec/tau[0],'k', linewidth=1.8)
    
    plt.plot((fexpM166[:,1])/del0M166,fexpM166[:,0]*tsec/tau[1],'r', linewidth=1.8, label=r'$M=1.66$')
    plt.plot((fexpM166[:,2])/del0M166,fexpM166[:,0]*tsec/tau[1],'r', linewidth=1.8, )
    
    plt.plot((fexpM145[:,1])/del0M145,fexpM145[:,0]*tsec/tau[2],'b', linewidth=1.8, label=r'$M=1.45$')
    plt.plot((fexpM145[:,2])/del0M145,fexpM145[:,0]*tsec/tau[2],'b', linewidth=1.8, )
    

    ax.set_xlabel(r'$\mathbf{x/L}$',fontsize=18)
    ax.set_ylabel(r'$\mathbf{tu_s/L}$',fontsize=18)
#    ax.set_ylabel(r'$\mathbf{t^*}$',fontsize=18)

def pfplot():
    plt.figure(1)
    plt.plot((f[:,0]-x_curt)/curt_width,f[:,2]*1e6,'b',linewidth=1.8)
    plt.plot((f[:,1]-x_curt)/curt_width,f[:,2]*1e6,'r',linewidth=1.8)

    ax.set_xlabel(r'$\mathbf{x^*}$',fontsize=18)
    ax.set_ylabel(r'$\mathbf{t^*}$',fontsize=18)

def sep_scaledplot(indx):
    plt.figure(2)
    
    plt.plot((fexpM192[:,1]-fexpM192[:,2])/del0M192,fexpM192[:,0]*tsec/tau[0],'k', linewidth=1.8, label=r'$M=1.92$')
    plt.plot((fexpM166[:,1]-fexpM166[:,2])/del0M166,fexpM166[:,0]*tsec/tau[1],'r', linewidth=1.8, label=r'$M=1.66$')
    plt.plot((fexpM145[:,1]-fexpM145[:,2])/del0M145,fexpM145[:,0]*tsec/tau[2],'b', linewidth=1.8, label=r'$M=1.45$')

    ax.set_xlabel(r'$\mathbf{\delta}_x/\mathbf{\delta}_o$',fontsize=18)
    ax.set_ylabel(r'$\mathbf{tu_2/L}$',fontsize=18)
    ax.set_ylabel(r'$\mathbf{t^*}$',fontsize=18)
    #plt.ylabel(r'$\mathbf{x^*}$',fontsize=18)
    #plt.plot(fM124_1815[:,2]*tsec/tau[3],1+1.5*(fM124_1815[:,2]*tsec/tau[3])**2,'--k',linewidth=1.8)
    #plt.plot(f[:,2]*tsec/tau,-1.5+3.5*f[:,2]*tsec/tau,'--r',linewidth=1.8)

for indx,i in enumerate(range(1,2)):
# Experimental data
    dirparts = (os.getcwd(),'/Experiments','/PVF21_M1pt66.mat')
    fileM166 = "".join(dirparts)
    fexpM166 = spio.loadmat(fileM166)
    fexpM166 = fexpM166['PVF21_M1pt66']
    del0M166 = fexpM166[0,1]-fexpM166[0,2]

    dirparts = (os.getcwd(),'/Experiments','/PVF23_M1pt45.mat')
    fileM145 = "".join(dirparts)
    fexpM145 = spio.loadmat(fileM145)
    fexpM145 = fexpM145['PVF23_M1pt45']
    del0M145 = fexpM145[0,1]-fexpM145[0,2]

    dirparts = (os.getcwd(),'/Experiments','/PVF21_M1pt92.mat')
    fileM192 = "".join(dirparts)
    fexpM192 = spio.loadmat(fileM192)
    fexpM192 = fexpM192['PVF21_M1pt92']
    del0M192 = fexpM192[0,1]-fexpM192[0,2]

    taus(1)
    ax = plt.gca()

#    pfplot()
    pf_scaledplot(indx)
    sep_scaledplot(indx)
#    sepplot()


#ax.set_xlim([-0.3,35])
#ax.set_xlim([0,20])
#ax.set_xticks(range(0,21,5))
#ax.set_xlim([-0.001,3])
#ax.set_ylim([0.0,12])
#ax.set_ylim([0.0,250])
#ax.set_ylim([0.0,140])
ax.tick_params(labelsize=16)
#ax.legend(['3D'],loc='center right')
ax.legend()
#plt.grid()
plt.tight_layout()
#ax.set_aspect('equal')
plt.show()


