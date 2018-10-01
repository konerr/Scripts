#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import sys
import os,glob
from itertools import islice

plt.rc('text', usetex=True)
plt.rc('font', weight='bold')
plt.rc('axes', linewidth=1.6)
plt.rc('lines', linewidth=1.8)
plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)
plt.rc('font',**{'family':'sans-serif', 'weight':'bold'})
plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

Ms = 3.0 ;
p = 101325 ;
rho = 1.2048 ;
gamma = 1.4 ;
R = 287.0
us = Ms*np.sqrt(gamma*p/rho) ;
dp = 100E-6 ;
tau = dp/us ;
x_shock = 0.12
x_curt = 0.15
curt_width = 3.5e-3
phi = 0.10
rho2 = 4.64670
p2 = 1047025.0
u2 = 7.625535638079468E+02
#rho2 = 1
#p2=1
#u2=1
phis = [10.0,15.0,20.0,25.0]

lines = ['r','b','k','g'] #Fucked up order due to filenames
syms1 = ['sr','sk','sg','sb']
syms2 = ['--r','--b','--k','--g']
syms3 = ['o-r','o-b','o-k','o-g']
syms4 = ['x-r','x-b','x-g','x-c']
syms5 = ['or','ob','ok','og']
syms6 = ['^r','^b','^k','^g']
syms7 = ['-.r','-.b','-.k','-.g']

#sd2dparts = (os.getcwd(),'/2D_SD')
dirsd2d = "".join(os.getcwd())
#mes10_dp1 = sorted(glob.glob('../100micro-All/Mesoscale/NoFluc/phi10/*forces*'))
mes10_dp1 = sorted(glob.glob('Mesoscale/NoFluc/tests/dp1mic/*forces*'))

files = [mes10_dp1]

max_rho = np.zeros((2))
p1indx = range(0,3*len(files),3)
p2indx = range(1,3*len(files),3)
p3indx = range(2,3*len(files),3)

def plot_meso(j,lindx,leg):
    if leg == 1:
        legs = lines
    elif leg == 2:
        legs = syms2
    elif leg == 3:
        legs = syms3
    elif leg == 4:
        legs = syms4
    elif leg == 5:
        legs = syms5
    elif leg == 6:
        legs = syms6
    elif leg == 7:
        legs = syms7

    plt.figure(p1indx[j])
    #plt.plot(x_nd,f[:,5]/f[1,5],label=r't/\tau=%d' % t )
    plt.plot(x_nd,f[:,5]/f[1,5],legs[lindx])
#    plt.plot(x_nd,f[:,5]/u2,legs[lindx])
    #plt.plot(x_nd,fMa,legs[lindx])
    plt.xlim([-5.0,15.0])
#    plt.ylim([0.0,1.2])
    plt.xlabel(r'$\boldsymbol{x/d_p}$', fontsize=16)
    #plt.ylabel(r'$\boldsymbol{Ma}$', fontsize=16)
    plt.ylabel(r'$\boldsymbol{u}$', fontsize=16)
    plt.title(r'$ \boldsymbol{\phi_p= %d\%%} $ ' % phis[j])
    plt.tight_layout()

    plt.figure(p2indx[j])
    plt.plot(x_nd,f[:,2]/f[1,2],legs[lindx])
#    plt.plot(x_nd,f[:,2]/p2,legs[lindx])
    plt.xlim([-5.0,15.0])
#    plt.ylim([0.0,3.5])
    plt.xlabel(r'$\boldsymbol{x/d_p}$', fontsize=16)
    plt.ylabel(r'$\boldsymbol{p}$', fontsize=16)
    plt.title(r'$ \boldsymbol{\phi_p= %d\%%} $ ' % phis[j])
    plt.tight_layout()
    #plt.plot(x_nd,f[:,2]/f[1,2],label=r'$t/\tau=%d$' % t )

    fig = plt.figure(p3indx[j])
    ax1 = fig.add_subplot(1,1,1)
    ax2 = ax1.twinx()
#    fig, ax1 = plt.subplots()
#    plt.plot(x_nd,f[:,1]/f[1,1]/(1-f[:,8]),lines[lindx])
#    plt.plot(x_nd,f[:,1]/f[1,1],lines[lindx])
    ax1.plot(x_nd,f[:,1]/f[1,1],lines[lindx])
#    plt.plot(x_nd,f[:,1]/rho2,lines[lindx])
#    plt.xlim([-5.0,15.0])
    ax1.set_xlim([-5.0,15.0])
#    ax1.set_ylim([0.2,1.8])
    ax2.set_ylim([-0.01,0.12])
#    plt.ylim([0.0,2.5])
    ax2.plot(x_nd,f[:,8],'--k')
    ax1.set_xlabel(r'$\boldsymbol{x/d_p}$', fontsize=16)
    ax1.set_ylabel(r'$\boldsymbol{\rho}$', fontsize=16)
    ax2.set_ylabel(r'$\boldsymbol{\phi_p}$', fontsize=16)
    ax1.set_title(r'$ \boldsymbol{\phi_p= %d\%%} $ ' % phis[j])

def readTime():
    print(line)
    varOut = float(next(ffile))
    varOut = varOut*1e6
    return varOut

def readDim():
    print(line)
    varOut = int((next(ffile).split())[0])
    return varOut

def readData():
    print(line)
    varOut = np.zeros((arrDim)) 
    for k in range(0,int(arrDim/5)):
        tmp = ((next(ffile).split(',')))
        for j in range(0,5):
            varOut[j+5*k] = float(tmp[j])
    return varOut

def readData2():
    print(line)
    varOut = np.zeros((arrDim)) 
    for k in islice(ffile,int(arrDim/5)):
        print(k)
    print(k)
    return k

cst = 1
k = 0
for indx, i in enumerate(files[:]):

    print (i)
    with open(i[indx],'r') as ffile:
        for count, line in enumerate(ffile):
            if line.startswith('# Physical time'):
                t = readTime()
                print(t)
            if line.startswith('# Dimensions'):
                arrDim = readDim()
                print(arrDim)
            if line.startswith('# Pcl x-coordinate'):
                x = readData()
            if line.startswith('# Pcl y-coordinate'):
                y = readData()
            if line.startswith('# Pcl z-coordinate'):
                z = readData()
            if line.startswith('# QS force x'):
                qsx = readData()
            if line.startswith('# QS force y'):
                qsy = readData()
            if line.startswith('# QS force z'):
                qsz = readData()
            if line.startswith('# PG force x'):
                pgx = readData()
            if line.startswith('# PG force y'):
                pgy = readData()
            if line.startswith('# PG force z'):
                pgz = readData()
            if line.startswith('# IU force x'):
                iux = readData()
            if line.startswith('# IU force y'):
                iuy = readData()
            if line.startswith('# IU force z'):
                iuz = readData()
            if line.startswith('# VU force x'):
                vux = readData()
            if line.startswith('# VU force y'):
                vuy = readData()
            if line.startswith('# VU force z'):
                vuz = readData()
            if line.startswith('# Total force x'):
                fx = readData()
            if line.startswith('# Total force y'):
                fy = readData()
            if line.startswith('# Total force z'):
                fz = readData()

#    f = np.genfromtxt(i)
#    #x_nd = (f[:,0]-0.001078)/dp
#    x_nd = (f[:,0]-0.001-0*dp)/dp
#
#    j = 0
#    a = np.sqrt(gamma*R*f[:,3])
#    fMa = np.divide(f[:,4],a) 
#    plot_meso(j,lindx,1)
#    lindx = lindx+1


#plt.legend(['Parmar',r'$C_d=1.0$',r'$C_d=0.04$',r'$C_d=0.0$','1-Way','DNS'])
#plt.xlabel(r'$\boldsymbol{x/d_p}$',fontsize=16)
#plt.ylabel(r'$\boldsymbol{t/\tau}$',fontsize=16)
#plt.tight_layout()
#plt.legend(['Meso','','Micro'])
#plt.show()
#plt.clf()

