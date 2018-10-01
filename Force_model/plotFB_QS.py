#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import sys
import os,glob

plt.rc('text', usetex=True)
plt.rc('font', weight='bold')
plt.rc('axes', linewidth=1.6)
plt.rc('lines', linewidth=1.8)
plt.rc('xtick', labelsize=46)
plt.rc('ytick', labelsize=46)
plt.rc('font',**{'family':'sans-serif', 'weight':'bold'})
plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

Ms = 3.0 ;
p = 101325 ;
rho = 1.2048 ;
gamma = 1.4 ;
us = Ms*np.sqrt(gamma*p/rho) ;
dp = 100E-6 ;
tau = dp/us ;
x_shock = 0.12
x_curt = 0.15
curt_width = 3.5e-3
phi = 0.10

phis = [10,15,20,25]

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
#files2d = sorted(os.listdir(dirsd2d))
#pg_nf_2way = sorted(glob.glob('FixPG_NoFluc_2way/*.yzavg*'))
#nf_2way = sorted(glob.glob('NoFluc_2way/*.yzavg*'))
mes10_cd1 = sorted(glob.glob('Mesoscale/NoFluc/tests/phi10_cdTest/cd1/*.yzavg*'))
mes10_cd2 = sorted(glob.glob('Mesoscale/NoFluc/tests/phi10_cdTest/cd07/*.yzavg*'))
mes10_cd3 = sorted(glob.glob('Mesoscale/NoFluc/tests/phi10_cdTest/cd04/*.yzavg*'))
mes10_cd4 = sorted(glob.glob('Mesoscale/NoFluc/tests/phi10_cdTest/cd01/*.yzavg*'))
mes10_cd5 = sorted(glob.glob('Mesoscale/NoFluc/tests/phi10_cdTest/oneway/*.yzavg*'))
mes10_cd6 = sorted(glob.glob('Mesoscale/NoFluc/tests/phi10_cdTest/cd004/*.yzavg*'))
mes10_cd7 = sorted(glob.glob('Mesoscale/NoFluc/tests/phi10_cdTest/cd001/*.yzavg*'))
mes10_cd8 = sorted(glob.glob('Mesoscale/NoFluc/tests/phi10_cdTest/cd0/*.yzavg*'))
mes10 = sorted(glob.glob('Mesoscale/NoFluc/phi10/*.yzavg*'))
mes15 = sorted(glob.glob('Mesoscale/NoFluc/phi15/*.yzavg*'))
mes20 = sorted(glob.glob('Mesoscale/NoFluc/phi20/*.yzavg*'))
mes25 = sorted(glob.glob('Mesoscale/NoFluc/phi25/*.yzavg*'))
mic10 = sorted(glob.glob('MicroData/Data_For_Rahul/10/*.dat'))
mic15 = sorted(glob.glob('MicroData/Data_For_Rahul/15/*.dat'))
mic20 = sorted(glob.glob('MicroData/Data_For_Rahul/20/*.dat'))
mic25 = sorted(glob.glob('MicroData/Data_For_Rahul/25/*.dat'))
#files = [mes10,mes15,mes20,mes25,mes10_cd1]
files = [mes10]
mes_cd = [mes10_cd1]
mes_cd07 = [mes10_cd2]
mes_cd04 = [mes10_cd3]
mes_cd01 = [mes10_cd4]
mes_oneway = [mes10_cd5]
mes_cd004 = [mes10_cd6]
mes_cd001 = [mes10_cd7]
mes_cd0 = [mes10_cd8]
#mic = [mic10,mic15,mic20,mic25]
mic = [mic10]

max_rho = np.zeros((2))
p1indx = range(0,2*len(files),2)
p2indx = range(1,2*len(files),2)

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
    plt.xlim([-5.0,15.0])
    plt.ylim([0.0,1.2])
    plt.xlabel(r'$\boldsymbol{x/d_p}$', fontsize=46)
    plt.ylabel(r'$\boldsymbol{u}$', fontsize=46)
    plt.title(r'$ \boldsymbol{\phi_p= %d\%%} $ ' % phis[j], fontsize=40)
    plt.tight_layout()
#    plt.figure(p2indx[j])
#    plt.plot(x_nd,f[:,2]/f[1,2],legs[lindx])
#    plt.plot(x_nd,f[:,1]/f[1,1]/(1-f[:,8]),lines[lindx])
#    plt.xlim([-5.0,15.0])
#    plt.ylim([0.0,2.5])
#    plt.ylim([0.0,3.5])
#    plt.xlabel(r'$\boldsymbol{x/d_p}$', fontsize=16)
#    plt.ylabel(r'$\boldsymbol{p}$', fontsize=16)
#    plt.ylabel(r'$\boldsymbol{\rho}$', fontsize=16)
#    plt.title(r'$ \boldsymbol{\phi_p= %d\%%} $ ' % phis[j])
#    plt.tight_layout()
    #plt.plot(x_nd,f[:,2]/f[1,2],label=r'$t/\tau=%d$' % t )
# 	plt.plot(f[:,0],f[:,3]/T, syms2[indx])
# 	plt.plot(f[:,0],f[:,8]/phi, syms2[indx])


#for j in range(1,(len(files)%1)+2):
for j in range(0,len(files)):
    lindx = 0
    files[j].pop(2)
    for indx, i in enumerate(files[j][1:2]):
        temp = i.split('.yzavg_')
        temp = temp[1].replace('.dat','')
        t = float(temp)/1e-7
    
        currfileparts = (dirsd2d,"/",i)
        currfile = "".join(currfileparts)
#        print (currfile)
    
        f = np.genfromtxt(currfile)
        x_nd = (f[:,0]-0.001078)/dp

        plot_meso(j,lindx,1)
        lindx = lindx+1

for j in range(0,len(mes_cd)):
#    print (j)
    lindx = 0
    mes_cd[j].pop(2)
    for indx, i in enumerate(mes_cd[j][1:2]):
#    for i in files[j]:
        temp = i.split('.yzavg_')
        temp = temp[1].replace('.dat','')
        t = float(temp)/1e-7
#        print (t)
##        t = int(t)
    
    #	print (t,str(t))
    #	print ("%03d" % t)
        currfileparts = (dirsd2d,"/",i)
        currfile = "".join(currfileparts)
#        print (currfile)
    
        f = np.loadtxt(currfile)
        x_nd = (f[:,0]-0.001078)/dp
    
        plot_meso(j,lindx,2)
        lindx = lindx+1

#for j in range(0,len(mes_cd07)):
#    lindx = 0
#    mes_cd07[j].pop(2)
#    for indx, i in enumerate(mes_cd07[j][1:2]):
#        temp = i.split('.yzavg_')
#        temp = temp[1].replace('.dat','')
#        t = float(temp)/1e-7
#    
#        currfileparts = (dirsd2d,"/",i)
#        currfile = "".join(currfileparts)
##        print (currfile)
#    
#        f = np.loadtxt(currfile)
#        x_nd = (f[:,0]-0.001078)/dp
#
#        plot_meso(j,lindx,1)
#        lindx = lindx+1
#
#for j in range(0,len(mes_cd001)):
#    lindx = 0
#    mes_cd001[j].pop(2)
#    for indx, i in enumerate(mes_cd001[j][1:2]):
#        temp = i.split('.yzavg_')
#        temp = temp[1].replace('.dat','')
#        t = float(temp)/1e-7
#    
#        currfileparts = (dirsd2d,"/",i)
#        currfile = "".join(currfileparts)
##        print (currfile)
#    
#        f = np.loadtxt(currfile)
#        x_nd = (f[:,0]-0.001078)/dp
#
#        plot_meso(j,lindx,1)
#        lindx = lindx+1


for j in range(0,len(mes_cd04)):
    lindx = 0
    mes_cd04[j].pop(2)
    for indx, i in enumerate(mes_cd04[j][1:2]):
        temp = i.split('.yzavg_')
        temp = temp[1].replace('.dat','')
        t = float(temp)/1e-7
    
        currfileparts = (dirsd2d,"/",i)
        currfile = "".join(currfileparts)
#        print (currfile)
    
        f = np.loadtxt(currfile)
        x_nd = (f[:,0]-0.001078)/dp

        plot_meso(j,lindx,3)
        lindx = lindx+1

for j in range(0,len(mes_cd0)):
    lindx = 0
    mes_cd0[j].pop(2)
    for indx, i in enumerate(mes_cd0[j][1:2]):
        temp = i.split('.yzavg_')
        temp = temp[1].replace('.dat','')
        t = float(temp)/1e-7
    
        currfileparts = (dirsd2d,"/",i)
        currfile = "".join(currfileparts)
        print (currfile)
    
        f = np.loadtxt(currfile)
        x_nd = (f[:,0]-0.001078)/dp

        plot_meso(j,lindx,4)
        lindx = lindx+1


for j in range(0,len(mes_oneway)):
    lindx = 0
    mes_oneway[j].pop(2)
    for indx, i in enumerate(mes_oneway[j][1:2]):
        temp = i.split('.yzavg_')
        temp = temp[1].replace('.dat','')
        t = float(temp)/1e-7
    
        currfileparts = (dirsd2d,"/",i)
        currfile = "".join(currfileparts)
        print (currfile)
    
        f = np.loadtxt(currfile)
        x_nd = (f[:,0]-0.001078)/dp

        plot_meso(j,lindx,5)
        lindx = lindx+1



#for indx, i in enumerate(mic10[1:2]):
for j in range(0,len(mic)):
    syms1indx = 0
    for indx, i in enumerate(mic[j][3:4]):
            currfileparts = (dirsd2d,"/",i)
            currfile = "".join(currfileparts)
#            print (currfile)
        
    #        f = np.loadtxt(currfile)
            f = np.genfromtxt(currfile, delimiter='\t', dtype=np.complex128)
            x_nd = (f[:,0]/dp)+7.8
        #        plt.figure(1)
        #	plt.plot(f[:,0],f[:,1]/rho, lines[indx],label='t=%d' % t )
        ##        plt.figure(2)
        #	plt.plot(f[:,0],f[:,5]/u, syms[indx])
        #	plt.plot(f[:,0],f[:,2]/p, syms1[indx])
            plt.figure(p1indx[j])
            plt.plot(x_nd,f[:,34], syms1[syms1indx], markerfacecolor='none',label='DNS')  # rho=31,p=32,u=34
            plt.xlim([-5.0,15.0])
#            plt.figure(p2indx[j])
#            plt.plot(x_nd,f[:,32], syms1[syms1indx], markerfacecolor='none')
#            plt.xlim([-5.0,15.0])
            syms1indx = syms1indx+1 


plt.legend(['Parmar',r'$C_d=1.0$',r'$C_d=0.04$',r'$C_d=0.0$','1-Way','DNS'],
		prop={'size': 24})
plt.show()
plt.clf()

