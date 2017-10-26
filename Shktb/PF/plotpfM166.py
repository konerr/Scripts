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

Ms = 1.66 
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
curt_width = 2e-3
dp = 115e-6
rhop = 2500.0
phi = range(14,20)
tsec = 1e0

syms = ['r','b','g','--r','--b','--g']

# Compute P_wall Theofanous JFM 2016
#def compPwall():
#    global pwall
a = 1.0
b = -(2+0.5*gamma*(gamma+1)*Ms**2)
c = 1-0.5*gamma*(gamma-1)*Ms**2
eta = np.roots([a,b,c])
print (eta[0],eta[1])
eta = max(eta)
pwall = eta*p

if pwall/p1 <= 1:
	print ('Pwall is too small, check the expression...')
	sys.exit(1)

def taus(tindx):
#    compPwall()
    global tau
# Time scale based on post-shock velocity 
# Ling et. al Phys of Fluids 2012
    if tindx == 1:
        tau = curt_width/us 
    elif tindx == 2:
# Theofanous JFM 2016
        und = np.sqrt( (p1/rhop)*((pwall/p1)-1) )
        tau = curt_width/und

def pf_scaledplot(indx):
    plt.figure(1)
    plt.plot((f[:,0]-x_curt)/curt_width,f[:,2]*tsec/tau,syms[indx],linewidth=1.8,label=r'$\phi_p = $ %s \%%'  % i) 
    plt.plot((f[:,1]-x_curt)/curt_width,f[:,2]*tsec/tau,syms[indx],linewidth=1.8)
#    label=r'$p = $ %i' % i if leg==1 else ""

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
    plt.figure(1)
 #   plt.plot(f[:,2]*tsec/tau,(f[:,1]-f[:,0])/curt_width,syms[indx],linewidth=1.8,label=r'$\phi_p = $ %s \%%'  % i)
    plt.plot((f[:,1]-f[:,0])/curt_width,f[:,2]*tsec/tau*np.sqrt(phi[indx]*0.01),syms[indx],linewidth=1.8,label=r'$\phi_p = $ %s \%%'  % i)

    ax.set_xlabel(r'$\mathbf{\delta}_x/\mathbf{\delta}_o$',fontsize=18)
    ax.set_ylabel(r'$\mathbf{tu_2/L}$',fontsize=18)
    ax.set_ylabel(r'$\mathbf{t^*}$',fontsize=18)
    #plt.ylabel(r'$\mathbf{x^*}$',fontsize=18)
    #plt.plot(fM124_1815[:,2]*tsec/tau[3],1+1.5*(fM124_1815[:,2]*tsec/tau[3])**2,'--k',linewidth=1.8)
    #plt.plot(f[:,2]*tsec/tau,-1.5+3.5*f[:,2]*tsec/tau,'--r',linewidth=1.8)

for indx,i in enumerate(range(14,20)):
    dirparts = (os.getcwd(),'/2D/M166','/M166_pf_small')
    dirs = "".join(dirparts)
    currfileparts = (dirs,"/20_",str(i),"/pfLagrangian.dat")
    currfile = "".join(currfileparts)
#    print (currfile)

    f = np.loadtxt(currfile)

    taus(2)
    ax = plt.gca()
#    ax1 = plt.subplot(111)
#    ax2 = plt.subplot(111)

#    pfplot()
#    pf_scaledplot(indx)
    sep_scaledplot(indx)
#    sepplot()
#    if indx % 2 == 0:
#        ax.legend([r'$\phi_p=$ %i' % i ])
#        ax.legend([r'$18$' r'\%'])

# Experimental data
dirparts = (os.getcwd(),'/Experiments','/PVF21_M1pt66.mat')
fileM166 = "".join(dirparts)
fexpM166 = spio.loadmat(fileM166)
fexpM166 = fexpM166['PVF21_M1pt66']
del0 = fexpM166[0,1]-fexpM166[0,2]
plt.figure(1)
#plt.plot((fexpM166[:,1])/del0,fexpM166[:,0]*tsec/tau,'-.k', linewidth=1.8)
#plt.plot((fexpM166[:,2])/del0,fexpM166[:,0]*tsec/tau,'-.k', linewidth=1.8, label='Exp')

#plt.figure(2)
#plt.plot(fexpM166[:,0]*tsec/tau,(fexpM166[:,1]-fexpM166[:,2])/del0,'-.k', linewidth=1.8, label='Exp')
phis = np.sqrt(0.21)
plt.plot((fexpM166[:,1]-fexpM166[:,2])/del0,fexpM166[:,0]*tsec/tau*phis,'-.k', linewidth=1.8, label='Exp')
    

#ax.set_xlim([-0.3,35])
#ax.set_xlim([0,20])
ax.set_xticks(range(0,21,5))
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


