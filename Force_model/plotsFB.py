#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import sys
import os,glob

plt.rc('text', usetex=True)
plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath} \usepackage{sfmath} \boldmath "]
#plt.rc('font', weight='bold')
plt.rc('axes', linewidth=1.6)
plt.rc('lines', linewidth=2.8)
plt.rcParams['lines.markersize'] = 12
plt.rc('xtick', labelsize=40)
plt.rc('ytick', labelsize=40)
#plt.rc('font',**{'family':'sans-serif', 'weight':'bold'})
plt.clf()
plt.ion()

Ms = 3.0
p = 101325
rho = 1.2048
gamma = 1.4
R = 287.0
us = Ms*np.sqrt(gamma*p/rho) 
dp = np.array([100E-6, 10e-6, 5e-6, 1e-6])
dp = np.array([100E-6])
tau = dp/us 
x1_shock = 0.12
x_curt = 0.15
curt_width = 3.5e-3
phi = 0.10
rho2 = 4.64670
p2 = 1047025.0
u2 = 7.625535638079468E+02
#rho2 = 1
#p2=1
#u2=1
#phis = [10.0,15.0,20.0,25.0]
phis = [10.0]

#sd2dparts = (os.getcwd(),'/2D_SD')
dirsd2d = "".join(os.getcwd())
#files2d = sorted(os.listdir(dirsd2d))
#pg_nf_2way = sorted(glob.glob('FixPG_NoFluc_2way/*.yzavg*'))
#nf_2way = sorted(glob.glob('NoFluc_2way/*.yzavg*'))
mes10_sd = sorted(glob.glob('Mesoscale/NoFluc/phi10/*.SDyzavg*'))
mes15_sd = sorted(glob.glob('Mesoscale/NoFluc/phi15/*.SDyzavg*'))
mes20_sd = sorted(glob.glob('Mesoscale/NoFluc/phi20/*.SDyzavg*'))
mes25_sd = sorted(glob.glob('Mesoscale/NoFluc/phi25/*.SDyzavg*'))
mes10_cd5 = sorted(glob.glob('Mesoscale/NoFluc/phi10_cdTest/oneway/*.yzavg*'))
mes10_cd6 = sorted(glob.glob('Mesoscale/NoFluc/phi10_cdTest/cd004/*.yzavg*'))
mes10_cd7 = sorted(glob.glob('Mesoscale/NoFluc/phi10_cdTest/cd001/*.yzavg*'))
mes10_cd8 = sorted(glob.glob('Mesoscale/NoFluc/phi10_cdTest/cd0/*.yzavg*'))
mes10 = sorted(glob.glob('Mesoscale/NoFluc/tests/phi10_N4e4/*.yzavg*'))
mes10_intrp1 = sorted(glob.glob('Mesoscale/NoFluc/tests/phi10_intrp1/*.yzavg*'))
mes10_no_qs = sorted(glob.glob('Mesoscale/NoFluc/tests/phi10_no_qs/*.yzavg*'))
mes10_no_qs_intrp1 = sorted(glob.glob('Mesoscale/NoFluc/tests/phi10_no_qs_intrp1/*.yzavg*'))
mes10_no_qs2 = sorted(glob.glob('Mesoscale/NoFluc/tests/phi10_no_qs2/*.yzavg*'))
mes10_qs = sorted(glob.glob('Mesoscale/NoFluc/tests/phi10_qs/*.yzavg*'))
mes10_cdinv = sorted(glob.glob('Mesoscale/NoFluc/tests/phi10_cdinv/*.yzavg*'))
mes10_cdinv_phicorr = \
sorted(glob.glob('Mesoscale/NoFluc/tests/phi10_cdinv_phicorr/*.yzavg*'))
#mes10_no_qs2 = sorted(glob.glob('NoQS_2way/*.yzavg*'))
mes10_N4e4_v2s = sorted(glob.glob('Mesoscale/NoFluc/tests/phi10_N4e4_v2/small/*.yzavg*'))
mes10_N4e4_v2 = sorted(glob.glob('Mesoscale/NoFluc/tests/phi10_N4e4_v2/*.yzavg*'))
mes10_shr = sorted(glob.glob('Mesoscale/NoFluc/tests/phi10_N4e4_sharp/*.yzavg*'))
mes10_dx100 = sorted(glob.glob('../100micro-All/Mesoscale/NoFluc/phi10/*.yzavg*'))
mes10_dp10_N6E4 = sorted(glob.glob('Mesoscale/NoFluc/tests/dp10mic_N6E4/*.yzavg*'))
mes10_dp10 = sorted(glob.glob('Mesoscale/NoFluc/tests/dp10mic/*.yzavg*'))
mes10_dp5 = sorted(glob.glob('Mesoscale/NoFluc/tests/dp5mic/*.yzavg*'))
mes10_dp1 = sorted(glob.glob('Mesoscale/NoFluc/tests/dp1mic/*.yzavg*'))
mes10_shock = sorted(glob.glob('Mesoscale/NoFluc/tests/phi10_shock/*.yzavg*'))
mes10_shock2 = sorted(glob.glob('Mesoscale/NoFluc/tests/phi10_shock2/*.yzavg*'))
mes10_shock3 = sorted(glob.glob('Mesoscale/NoFluc/tests/phi10_shock3/*.yzavg*'))
mes10_shock2_shr = sorted(glob.glob('Mesoscale/NoFluc/tests/phi10_shock2_shr/*.yzavg*'))
mes10_shock_shr = sorted(glob.glob('Mesoscale/NoFluc/tests/phi10_shock_shr/*.yzavg*'))
#mes10 = sorted(glob.glob('Mesoscale/NoFluc/phi10/*.yzavg*'))
mes15 = sorted(glob.glob('Mesoscale/NoFluc/phi15/*.yzavg*'))
mes10_new = mes10_cdinv
mes15_new = sorted(glob.glob('Mesoscale/NoFluc/phi15_new/*.yzavg*'))
mes20_new = sorted(glob.glob('Mesoscale/NoFluc/phi20_new/*.yzavg*'))
mes25_new = sorted(glob.glob('Mesoscale/NoFluc/phi25_new/*.yzavg*'))
mes25_cdinv_phi = sorted(glob.glob('Mesoscale/NoFluc/phi25_cdinv_phi/*.yzavg*'))
mes20 = sorted(glob.glob('Mesoscale/NoFluc/phi20/*.yzavg*'))
mes25 = sorted(glob.glob('Mesoscale/NoFluc/phi25/*.yzavg*'))
mic10 = sorted(glob.glob('MicroData/Data_For_Rahul/10/*.dat'))
mic15 = sorted(glob.glob('MicroData/Data_For_Rahul/15/*.dat'))
mic20 = sorted(glob.glob('MicroData/Data_For_Rahul/20/*.dat'))
mic25 = sorted(glob.glob('MicroData/Data_For_Rahul/25/*.dat'))
files = [mes10,mes10_dp10,mes10_dp5,mes10_dp1]
files = [mes10, mes10_cdinv, mes10_cdinv_phicorr]
files = [mes10_new,mes15_new,mes20_new, mes25_new]
files = [mes25_new, mes25_cdinv_phi]
filesSD = [mes10_sd,mes15_sd,mes20_sd,mes25_sd]
#files = filesSD
mes_oneway = [mes10_cd5]
mes_cd004 = [mes10_cd6]
mes_cd001 = [mes10_cd7]
mes_cd0 = [mes10_cd8]
mic = [mic10,mic15,mic20,mic25]
#mic = [mic10]

max_rho = np.zeros((2))
p1indx = range(0,3*len(files),3)
p2indx = range(1,3*len(files),3)
p3indx = range(2,3*len(files),3)

lines = ['r','b','k','g'] #Fucked up order due to filenames
syms1 = ['sr','sk','sg','sb']
syms3 = ['--r','--b','--k','--g']
syms7 = ['o-r','o-b','o-k','o-g']
syms4 = ['x-r','x-b','x-g','x-c']
syms5 = ['or','ob','ok','og']
syms6 = ['^r','^b','^k','^g']
syms2 = ['-.r','-.b','-.k','-.g']

fsize = 50

#plt.ion()
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
    
    xcst = 1e0
    plt.figure(p1indx[j])
    ax = plt.gca()
#    for tick in ax.xaxis.get_major_ticks():
#            tick.label1.set_fontsize(fontsize)
#            tick.label1.set_fontweight('bold')
#    for tick in ax.yaxis.get_major_ticks():
#            tick.label1.set_fontsize(fontsize)
#            tick.label1.set_fontweight('bold')

#    ax.tick_params(labelsize=40)
    #plt.plot(x_nd,f[:,5]/f[1,5],label=r't/\tau=%d' % t )
    plt.plot(x_nd*xcst,f[:,5]/f[1,5],legs[lindx])
#    plt.plot(x_nd,fMa/(np.sqrt(gamma)*fMa[0]),legs[lindx])
    #plt.plot(x_nd,fMa/(fMa[0]),legs[lindx])
#    plt.plot(x_nd,fMa,legs[lindx])
    plt.xlim([-5.0,15.0])
    plt.xlim([-1.9,10.7])
#    plt.xlim([-0.0004,0.0012])
#    plt.xlim([-0.4,1.2])
    plt.ylim([0.0,1.2])
#    plt.ylim([0.0,1.5])
#    plt.xlabel(r'$\boldsymbol{x/d_p}$', fontsize=fsize)
    plt.xlabel(r'$\mathbf{x/d_p}$', fontsize=fsize)
#    plt.xlabel(r'$\boldsymbol{x}$(mm)', fontsize=fsize)
#    plt.ylabel(r'$\boldsymbol{Ma}$', fontsize=fsize)
    plt.ylabel(r'$\mathbf{u}$', fontsize=fsize)
    plt.title(r'$ \boldsymbol{\phi_p= %d\%%} $ ' % phis[j], fontsize=fsize)
    plt.tight_layout()

    plt.figure(p2indx[j])
    plt.plot(x_nd*xcst,f[:,2]/f[1,2],legs[lindx])
    plt.xlim([-5.0,15.0])
#    plt.xlim([-0.0004,0.0012])
#    plt.xlim([-0.4,1.2])
    plt.ylim([0.0,3.5])
    plt.xlabel(r'$\boldsymbol{x/d_p}$', fontsize=fsize)
#    plt.xlabel(r'$\boldsymbol{x}$', fontsize=fsize)
#    plt.xlabel(r'$\boldsymbol{x}$(mm)', fontsize=fsize)
    plt.ylabel(r'$\boldsymbol{p}$', fontsize=fsize)
    plt.title(r'$ \boldsymbol{\phi_p= %d\%%} $ ' % phis[j], fontsize=fsize)
    plt.tight_layout()
    #plt.plot(x_nd,f[:,2]/f[1,2],label=r'$t/\tau=%d$' % t )

    plt.figure(p3indx[j])
#    plt.plot(x_nd,f[:,1]/f[1,1]/(1-f[:,8]),legs[lindx])
    plt.plot(x_nd*xcst,f[:,1]/f[1,1],legs[lindx])
    plt.xlim([-5.0,15.0])
    plt.xlim([-1.9,10.7])
#    plt.xlim([-0.0004,0.0012])
#    plt.xlim([-0.4,1.2])
    plt.ylim([0.0,2.5])
#    plt.ylim([0.08,1.86])
    plt.xlabel(r'$\boldsymbol{x/d_p}$', fontsize=fsize)
#    plt.xlabel(r'$\boldsymbol{x}$', fontsize=fsize)
#    plt.xlabel(r'$\boldsymbol{x}$(mm)', fontsize=fsize)
    plt.ylabel(r'$\boldsymbol{\rho}$', fontsize=fsize)
    plt.title(r'$ \boldsymbol{\phi_p= %d\%%} $ ' % phis[j], fontsize=fsize)
    plt.tight_layout()

#    fig = plt.figure(p3indx[j])
#    ax1 = fig.add_subplot(1,1,1)
#    ax2 = ax1.twinx()
#    fig, ax1 = plt.subplots()
#    ax1.plot(x_nd,f[:,1]/f[1,1],lines[lindx])
#    ax1.set_xlim([-5.0,15.0])
#    ax1.set_ylim([0.2,1.8])
#    ax2.set_ylim([-0.01,0.12])
#    ax2.plot(x_nd,f[:,8],'--k')
#    ax1.set_xlabel(r'$\boldsymbol{x/d_p}$', fontsize=24)
#    ax1.set_ylabel(r'$\boldsymbol{\rho}$', fontsize=24)
#    ax2.set_ylabel(r'$\boldsymbol{\phi_p}$', fontsize=20)
#    ax1.set_title(r'$ \boldsymbol{\phi_p= %d\%%} $ ' % phis[j], fontsize=24)
#    ax1.set_tight_layout()

#for j in range(1,(len(files)%1)+2):
#for j in range(0,len(files)-3):
cst = 1
for j in range(0,len(files),1):
    lindx = 0
    files[j].pop(2)
    for indx, i in enumerate(files[j][:]):
        temp = i.split('.yzavg_')
        temp = temp[1].replace('.dat','')
        t = float(temp)/1e-7
        ndt = t/tau*1e-7
        print(ndt)
    
        currfileparts = (dirsd2d,"/",i)
        currfile = "".join(currfileparts)
        print (i)
    
        f = np.genfromtxt(i)
#        x_nd = (f[:,0]-0.001078)/dp[0]
        x_nd = (f[:,0]-0.001-0*dp[0])/dp[0]
#        x_nd = (f[:,0]-f[100,0]-0*dp[j])/dp[j]

        j = 0
        a = np.sqrt(gamma*R*f[:,3])
        fMa = np.divide(f[:,4],a) 
        plot_meso(j,indx,cst)
        lindx = lindx+1

#        dx = f[11,0]-f[10,0]
#        rgrad = np.gradient((f[:,1]),dx)
#        x_shock = f[np.where(rgrad==np.min(rgrad)),0]
#        if x_shock.size > 1:
#            x_shock = np.mean(x_shock)
#        x_shock = (x_shock-0.001-0*dp)/dp#+7.8
#        print(x_shock)
#
#
##        plt.plot(x_nd,rgrad)
#        plt.plot(x_shock,t,'sr',markeredgewidth=2.,fillstyle='none',
#                        label='EL' if indx==0 else "")
#        x_refl = f[np.where(rgrad==np.max(rgrad)),0]
#        if t > 0:
#            if x_refl.size > 1:
#                x_refl = np.mean(x_refl)
#            x_refl = (x_refl-0.001-cst*dp)/dp#+7.8
#            plt.plot(x_refl,t,'sr',markeredgewidth=2.,fillstyle='none')
        
    cst = cst+1

#for j in range(0,len(mes_oneway)):
#    lindx = 0
#    mes_oneway[j].pop(2)
#    for indx, i in enumerate(mes_oneway[j][1:2]):
#        temp = i.split('.yzavg_')
#        temp = temp[1].replace('.dat','')
#        t = float(temp)/1e-7
#    
#        currfileparts = (dirsd2d,"/",i)
#        currfile = "".join(currfileparts)
#        print (currfile)
#    
#        f = np.loadtxt(currfile)
#        x_nd = (f[:,0]-0.001078)/dp
#
#        plot_meso(j,lindx,5)
#        lindx = lindx+1

def plot_micro(j,syms1indx):
    plt.figure(p1indx[j])
    plt.plot(x_nd,f[:,34], syms1[syms1indx], markerfacecolor='none',label='DNS')  # rho=31,p=32,u=34
#    plt.plot(x_nd,f[:,34]/a_mic, syms1[syms1indx], markerfacecolor='none',label='DNS')  # rho=31,p=32,u=34
    plt.xlim([-5.0,15.0])
    plt.figure(p2indx[j])
    plt.plot(x_nd,f[:,32], syms1[syms1indx], markerfacecolor='none')
    plt.xlim([-5.0,15.0])
    plt.figure(p3indx[j])
    plt.plot(x_nd,f[:,31], syms1[syms1indx], markerfacecolor='none')
    plt.xlim([-5.0,15.0])

#for indx, i in enumerate(mic10[1:2]):
for j in range(3,len(mic)-0):
#for j in range(1,2,1):
    syms1indx = 0
    t = 0
    for indx, i in enumerate(mic[j][:]):
            currfileparts = (dirsd2d,"/",i)
            currfile = "".join(currfileparts)
#            print (currfile)
        
    #        f = np.loadtxt(currfile)
            f = np.genfromtxt(currfile, delimiter='\t', dtype=np.complex128)
#            x_nd = (f[:,0])+0
#            x_nd = (f[:,0]/dp[0])+7.8
#            dx = np.real(x_nd[11])-np.real(x_nd[10])
#            rgrad = np.gradient(np.real(f[:,31]),dx)
#            x_shock = np.real(f[np.where(rgrad==np.min(rgrad)),0])
#            if j==3 and t == 12:
#                rgrad_indx = np.argsort(rgrad)
#                x_shock = np.real(f[rgrad_indx[2],0])
#
#            x_shock = (x_shock/dp)+7.8
#            plt.plot(x_shock,t,'ok',markeredgewidth=2.,fillstyle='none',
#                        label='PR-DNS' if indx==0 else "")
#            if t > 0:
#                x_refl = np.real(f[np.where(rgrad==np.max(rgrad)),0])
#                x_refl = (x_refl/dp)+7.8
#                plt.plot(x_refl,t,'ok',markeredgewidth=2.,fillstyle='none')
#            print(x_shock)
#            t = t+4
#         plt.figure(1)
#        plt.plot(f[:,0],f[:,1]/rho, lines[indx],label='t=%d' % t )
#         plt.figure(2)
#        plt.plot(f[:,0],f[:,5]/u, syms[indx])
#        plt.plot(f[:,0],f[:,2]/p, syms1[indx])
#            a_mic = np.sqrt(f[:,32]/f[:,31])
#            plot_micro(j,syms1indx)
            syms1indx = syms1indx+1 

#plt.legend(['Parmar',r'$C_d=1.0$',r'$C_d=0.04$',r'$C_d=0.0$','1-Way','DNS'])
plt.xlabel(r'$\boldsymbol{x/d_p}$',fontsize=fsize)
plt.ylabel(r'$\boldsymbol{t/\tau}$',fontsize=fsize)
plt.title(r'$\boldsymbol{\phi_p=25\%}$',fontsize=fsize)
plt.tight_layout()
#plt.legend(['EL','PR-DNS'])
plt.legend(loc='best', prop={'size': 32}, frameon=False)
#plt.show()
#plt.clf()

