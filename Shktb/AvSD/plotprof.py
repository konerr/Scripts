#!/usr/bin/python

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

# File Name : plotprof.py

# Purpose :

# Creation Date : 22-01-2018

# Last Modified :

# Created By : Rahul Koneru 

#_._._._._._._._._._._._._._._._._._._._._.

import matplotlib.pyplot as plt
import numpy as np
import scipy.io as spio
import os

plt.rc('text', usetex=True)
plt.rc('font', weight='bold')
plt.rc('axes', linewidth=2.0)
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
plt.rc('lines', linewidth=2.8)
plt.rcParams['lines.markersize'] = 12
plt.rc('xtick', labelsize=40)
plt.rc('ytick', labelsize=40)
#plt.rc('font',**{'family':'sans-serif', 'weight':'bold'})
plt.rcParams["figure.figsize"] = [12.8,9.8]
plt.clf()

basedir = os.getcwd()
pfL = '/pfLagrangian.dat'
pfE = '/pfEulerian.dat'
fL1Dparts = (basedir,'/1D/200_21',pfL)
fE1Dparts = (basedir,'/1D/200_21',pfE)
fL2Dparts = (basedir,'/2D/200_21',pfL)
fE2Dparts = (basedir,'/2D/200_21',pfE)
fL2Dsparts = (basedir,'/2D/200_21_short',pfL)
fL3Dparts = (basedir,'/3D/20_21',pfL)
fE3Dparts = (basedir,'/3D/20_21',pfE)

fE2D_TH_parts = (basedir,'/TH_M166_21_20',pfE)
fL2D_TH_parts = (basedir,'/TH_M166_21_20',pfL)

fL1D = "".join(fL1Dparts)
fE1D = "".join(fE1Dparts)
fL2D = "".join(fL2Dparts)
fE2D = "".join(fE2Dparts)
fL2Ds = "".join(fL2Dsparts)
fL3D = "".join(fL3Dparts)
fE3D = "".join(fE3Dparts)
fL2D_TH = "".join(fL2D_TH_parts)
fE2D_TH = "".join(fE2D_TH_parts)
files = [fL1D, fE1D, fL2D, fE2D, fL3D, fE3D, fL2Ds]
files = [fL2D_TH, fE2D_TH, fL3D, fE3D, fL2Ds]

#exp = spio.loadmat('/home/local/UFAD/rahul.koneru/post_processing/shktb/Experiments/PVF21_M1pt66.mat')
exp = spio.loadmat('../Post_shktb_experiments/PVF21_M1pt66.mat')
exp = exp['PVF21_M1pt66']
#f1D = np.genfromtxt(files[0])
#f2D = np.genfromtxt(files[2])
#f2Ds = np.genfromtxt(files[6])
#f3D = np.genfromtxt(files[4])
f2D_TH = np.genfromtxt(files[0])
f2Ds = np.genfromtxt(files[4])
f3D = np.genfromtxt(files[2])
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
curt_width = 2e-3
dp = 115e-6
rhop = 2500.0
phi = range(14,23,5)
phi = [14,19,23]#range(14,23,5)
tsec = 1e0
t = 1e6

syms  = ['--g','--b','--r']
lines = ['g','b','r']

msz = 18
lwd = 4.8

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
        print (und)
#        und = np.sqrt( p1*((pwall/p1)-1) )
        tau = curt_width/und

def pf_scaledplot(indx):
    plt.figure(1)
#    plt.plot((f[:,0]-x_curt)/curt_width,f[:,2]*tsec/tau,syms[indx],linewidth=1.8,label=r'$\phi_p = $ %s \%%'  % i) 
    plt.plot((f[:,0]-x_curt)/curt_width,(f[:,2]-53.33/t)*tsec/tau,syms[indx],linewidth=lwd) 
    plt.plot((f[:,1]-x_curt)/curt_width,(f[:,2]-53.33/t)*tsec/tau,lines[indx],linewidth=lwd)
#    label=r'$p = $ %i' % i if leg==1 else ""

    ax.set_xlabel(r'$\mathbf{x/L}$',fontsize=fsize)
    ax.set_ylabel(r'$\mathbf{tu_s/L}$',fontsize=fsize)
#    ax.set_ylabel(r'$\mathbf{t^*}$',fontsize=18)

def pfplot():
    plt.figure(1)
    plt.plot((f[:,0]-x_curt)/curt_width,f[:,2]*1e6-53.33,'b',linewidth=lwd)
    plt.plot((f[:,1]-x_curt)/curt_width,f[:,2]*1e6-53.33,'r',linewidth=lwd)

    ax.set_xlabel(r'$\mathbf{x^*}$',fontsize=fsize)
    ax.set_ylabel(r'$\mathbf{t^*}$',fontsize=fsize)

def sep_scaledplot(indx):
    plt.figure(1)
    #plt.plot((f[:,2]-53.33e-6)*tsec/tau,(f[:,1]-f[:,0])/curt_width,syms[indx],linewidth=1.8,label=r'$\phi_p = $ %s \%%'  % i)
    plt.plot((f[:,1]-f[:,0])/curt_width,(f[:,2]-53.33e-6)*tsec/tau,lines[indx],lw=lwd)
#    plt.plot((f[:,1]-f[:,0])/curt_width,f[:,2]*tsec/tau*np.sqrt(phi[indx]*0.01),syms[indx],linewidth=1.8,label=r'$\phi_p = $ %s \%%'  % i)

#    ax.set_xlabel(r'$\mathbf{\delta}_x/\mathbf{\delta}_o$',fontsize=fsize)
    ax.set_xlabel(r'$\mathbf{\delta}_x/\mathbf{L}$',fontsize=fsize)
    ax.set_ylabel(r'$\mathbf{tu_s/L}$',fontsize=fsize)
#    ax.set_ylabel(r'$\mathbf{t^*}$',fontsize=18)
    #plt.ylabel(r'$\mathbf{x^*}$',fontsize=18)
    #plt.plot(fM124_1815[:,2]*tsec/tau[3],1+1.5*(fM124_1815[:,2]*tsec/tau[3])**2,'--k',linewidth=1.8)
    #plt.plot(f[:,2]*tsec/tau,-1.5+3.5*f[:,2]*tsec/tau,'--r',linewidth=1.8)

def plotexp(ind):
    if ind == 0:
        plt.plot(exp[:,0]*t,exp[:,2]-exp[0,2],'--c',lw=lwd)
        plt.plot(exp[:,0]*t,exp[:,1]-exp[0,2],'c',lw=lwd)
    elif ind == 1:
        plt.plot((exp[:,2]-exp[0,2])/curt_width,exp[:,0]*t,'--c',lw=lwd)
        plt.plot((exp[:,1]-exp[0,2])/curt_width,exp[:,0]*t,'c',lw=lwd)
    elif ind == 2:
        plt.plot((exp[:,2]-exp[0,2])/curt_width,exp[:,0]*tsec/tau,'Pk',lw=lwd) 
        plt.plot((exp[:,1]-exp[0,2])/curt_width,exp[:,0]*tsec/tau,'^k',lw=lwd)
    elif ind == 3:
        plt.plot((exp[:,1]-exp[:,2])/curt_width,exp[:,0]*tsec/tau,'^k',lw=lwd) 

#files = [fL1D, fL2Ds, fL3D]
#files = [fL2D_TH, fL2Ds, fL3D]
files = [fL2D_TH, fL3D]
fsize = 50 
plt.clf()
plt.ion()
plt.figure(1)
ax =plt.gca()
taus(1)
plotexp(3)
for indx,ifl in enumerate(files):
    f = np.genfromtxt(ifl)
    taus(1)
#    pfplot()
#    pf_scaledplot(indx)
    sep_scaledplot(indx)

#    plt.plot(f[:,2]*t-53.33,f[:,0]-f[0,0],lw=lwd,label='UPF, 1D')
#    plt.plot(f[:,2]*t-53.33,f[:,1]-f[0,0],lw=lwd,label='DPF, 1D')
   
#plt.plot(f1D[:,2]*t-53.33,f1D[:,0]-f1D[0,0],'--b',lw=lwd,label='UPF, 1D')
#plt.plot(f1D[:,2]*t-53.33,f1D[:,1]-f1D[0,0],'b',lw=lwd,label='DPF, 1D')
#plt.plot(f2Ds[:,2]*t-53.33,f2Ds[:,0]-f2Ds[0,0],'--g',lw=lwd,label='UPF, 2D')
#plt.plot(f2Ds[:,2]*t-53.33,f2Ds[:,1]-f2Ds[0,0],'g',lw=lwd,label='DPF, 2D')
##plt.plot(f2Ds[:,2]*t-53.33,f2Ds[:,0]-f2Ds[0,0],'--k',lw=lwd,label='UPF, 2D-Short')
##plt.plot(f2Ds[:,2]*t-53.33,f2Ds[:,1]-f2Ds[0,0],'k',lw=lwd,label='DPF, 2D-Short')
#plt.plot(f3D[:,2]*t-53.33,f3D[:,0]-f3D[0,0],'--r',lw=lwd,label='UPF, 3D')
#plt.plot(f3D[:,2]*t-53.33,f3D[:,1]-f3D[0,0],'r',lw=lwd,label='DPF, 3D')
#plt.plot(exp[:,0]*t,exp[:,2]-exp[0,2],'--c',lw=lwd,label='UPF, EXP')
#plt.plot(exp[:,0]*t,exp[:,1]-exp[0,2],'c',lw=lwd,label='DPF, EXP')

#plt.xlim([-0.5,40])
plt.xlim([-0.0,20])
plt.ylim([0,250])
#plt.ylabel('x(m)',fontsize=fsize)
#plt.xlabel(r't($\mu$s)',fontsize=fsize)
#plt.figure(2)
#plt.plot(u[:,0],u[:,1],'k')
#ax.set_xticks(range(0,951,150))
#ax.set_xticks(range(0,50,10))
ax.set_xticks(range(0,25,5))
ax.set_yticks(range(0,300,50))
ax.tick_params(labelsize=40)
#ax.legend(['UPF, 1D','DPF, 1D','UPF, 2D','DPF, 2D','UPF, 3D','DPF, 3D',
#'UPF, Exp','DPF, Exp'],loc='lower right', prop={'size': 24}, frameon=False)
#ax.legend(['UPF, Exp','DPF, Exp','UPF, 1D','DPF, 1D','UPF, 2D','DPF, 2D','UPF, 3D','DPF, 3D'],loc='lower right', prop={'size': 24}, frameon=False)
#ax.legend(['UPF, Exp','DPF, Exp','UPF, TH','DPF, TH','UPF, RBNN','DPF, RBNN'],loc='lower right', prop={'size': 24}, frameon=False)
#ax.legend(['Exp','1D','2D', '3D'],loc='lower right',
#        prop={'size': 32}, frameon=False)
ax.legend(['Exp','TH','RBNN'],loc='lower right',
        prop={'size': 32}, frameon=False)
plt.tight_layout()
plt.grid(which='both')
#plt.show()
