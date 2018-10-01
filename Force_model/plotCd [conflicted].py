#!/usr/bin/python

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

# File Name : plotCd.py

# Purpose :

# Creation Date : 29-05-2018

# Last Modified :

# Created By : Rahul Koneru 

#_._._._._._._._._._._._._._._._._._._._._.

import matplotlib.pyplot as plt
import numpy as np

plt.rc('text', usetex=True)
plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath} \usepackage{sfmath} \boldmath "]
#plt.rc('font', weight='bold')
plt.rc('axes', linewidth=1.6)
plt.rc('lines', linewidth=2.0)
plt.rcParams['lines.markersize'] = 12
plt.rc('xtick', labelsize=30)
plt.rc('ytick', labelsize=30)
#plt.rc('font',**{'family':'sans-serif', 'weight':'bold'})

M_std = np.linspace(0.0, 0.60,num=10)
M_sub = np.linspace(0.6, 1.00, num=10)
M_sup = np.linspace(1.0, 1.75, num=10)
M = np.linspace(0.2, 1.75, num=10)
M_bs = [0.62, 0.72, 0.82, 0.89, 0.96, 1.05, 1.15, 1.25, 1.75]
Mcr = 0.6

def Cd_Re(Re):
    Cd_std  = 24.0/Re*(1.0+0.150*Re**(0.687)) + 0.4200/(1.0+42500.0/Re**(1.160))
    Cd_Mcr  = 24.0/Re*(1.0+0.150*Re**(0.684)) + 0.5130/(1.0+483.0/Re**(0.669))
    Cd_M1   = 24.0/Re*(1.0+0.118*Re**(0.813)) + 0.6900/(1.0+3550.0/Re**(0.793))
    Cd_M175 = 24.0/Re*(1.0+0.107*Re**(0.867)) + 0.6460/(1.0+861.0/Re**(0.634))
 
    return Cd_std, Cd_Mcr, Cd_M1, Cd_M175

def modelcd_parmar(M):
    if M <= Mcr:
        Cd = Cd_std + (Cd_Mcr-Cd_std)*M/Mcr
    elif (M > Mcr) & (M <= 1.0):
        f1 = -1.884+8.422*M-13.70*M*M+8.162*M*M*M
        f2 = -2.228+10.35*M-16.96*M*M+9.840*M*M*M
        f3 =  4.362-16.91*M+19.84*M*M-6.296*M*M*M        
        c1 = 6.48 ; c2 = 9.28 ; c3 = 12.21
        fac = ( f1*(lre-c2)*(lre-c3)/((c1-c2)*(c1-c3))
              + f2*(lre-c1)*(lre-c3)/((c2-c1)*(c2-c3)) 
              + f3*(lre-c1)*(lre-c2)/((c3-c1)*(c3-c2)) )
        Cd = Cd_Mcr + fac*(Cd_M1-Cd_Mcr)
    elif (M > 1.0) & (M <= 1.75):
        f1 = -2.963+4.392*M-1.169*M*M-0.027*M*M*M-0.233*np.exp((1.0-M)/0.011)
        f2 = -6.617+12.11*M-6.501*M*M+1.182*M*M*M-0.174*np.exp((1.0-M)/0.010)
        f3 = -5.866+11.57*M-6.665*M*M+1.312*M*M*M-0.350*np.exp((1.0-M)/0.012)
        c1 = 6.48 ; c2 = 8.93 ; c3 = 12.21
        fac = ( f1*(lre-c2)*(lre-c3)/((c1-c2)*(c1-c3))
              + f2*(lre-c1)*(lre-c3)/((c2-c1)*(c2-c3)) 
              + f3*(lre-c1)*(lre-c2)/((c3-c1)*(c3-c2)) )
        Cd = Cd_M1 + fac*(Cd_M175-Cd_M1)
    else :
        Cd = Cd_M175
   
    return Cd

def modelcd_sub(M):
    f1 = -1.884+8.422*M-13.70*M*M+8.162*M*M*M
    f2 = -2.228+10.35*M-16.96*M*M+9.840*M*M*M
    f3 =  4.362-16.91*M+19.84*M*M-6.296*M*M*M        
    c1 = 6.48 ; c2 = 9.28 ; c3 = 12.21
    fac = ( f1*(lre-c2)*(lre-c3)/((c1-c2)*(c1-c3))
          + f2*(lre-c1)*(lre-c3)/((c2-c1)*(c2-c3)) 
          + f3*(lre-c1)*(lre-c2)/((c3-c1)*(c3-c2)) )
    Cd = 0*Cd_Mcr + fac*(Cd_M1-Cd_Mcr)
    return Cd

def modelcd_sup(M):
    f1 = -2.963+4.392*M-1.169*M*M-0.027*M*M*M-0.233*np.exp((1.0-M)/0.011)
    f2 = -6.617+12.11*M-6.501*M*M+1.182*M*M*M-0.174*np.exp((1.0-M)/0.010)
    f3 = -5.866+11.57*M-6.665*M*M+1.312*M*M*M-0.350*np.exp((1.0-M)/0.012)
    c1 = 6.48 ; c2 = 8.93 ; c3 = 12.21
    fac = ( f1*(lre-c2)*(lre-c3)/((c1-c2)*(c1-c3))
          + f2*(lre-c1)*(lre-c3)/((c2-c1)*(c2-c3)) 
          + f3*(lre-c1)*(lre-c2)/((c3-c1)*(c3-c2)) )
    Cd = Cd_M1 + fac*(Cd_M175-Cd_M1) - Cd_Mcr
    return Cd

fsize = 40
plt.ion()
fig0 = plt.figure(0)
ax0 = fig0.add_subplot(111)
ax0.cla()
#fig1 = plt.figure(1)
#ax1 = fig1.add_subplot(111)
#ax1.cla()
for i in M_bs[:]:
    Re_min = 101*i*np.sqrt(0.7*np.pi)
    Re = np.linspace(Re_min, 1*1e6, num=20000)
    lre = np.log(Re)
    Cd_std, Cd_Mcr, Cd_M1, Cd_M175 = Cd_Re(Re)
    Cd = modelcd_parmar(i)
#    Cd = modelcd_sup(i)
#    Cd = modelcd_sub(i)
#    print('Re min=%4.3f for M=%3.2f, Max Cd=%3.2f' % (Re_min,i,max(Cd)))
    ax0.semilogx(Re, Cd, label='M=%3.2f' % i)
#    ax0.semilogx(Re, Cd_Mcr-Cd_, label='M=%3.2f' % i)

#np.set_printoptions(precision=5)
#print(Cd)
#print(Cd_M1)
#print(Cd_M175)
#print(Cd_Mcr)
#print(Cd_std)

#ymin = np.round(min(Cd_Mcr),3) 
#ymax = np.round(max(Cd_Mcr),3)
#ymin = ymin - 0.2*ymin
#ymax = ymax + 0.1*ymax
#plt.ylim([ymin, ymax])
ax0.set_xlim([1e2, max(Re)])
ax0.set_ylim([0.3, 1.7])
ax0.set_yticks(np.linspace(0.3,1.7,num=8))
ax0.set_xlabel('Re', fontsize=fsize)
ax0.set_ylabel(r'$C_{D}$', fontsize=fsize)
ax0.set_title('Parmar Model',fontsize=fsize)
ax0.legend(prop={'size':16})
#ax0.set_tight_layout()
#ax1.set_xlabel('Re', fontsize=fsize)
#ax1.set_ylabel(r'$C_{D,sub}$', fontsize=fsize)
#ax1.legend()
#ax1.set_tight_layout()
