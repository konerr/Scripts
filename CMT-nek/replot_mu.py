#!/usr/bin/python

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os

mpl.use('tkagg')
#plt.ion()
#mpl.rcParams['font.family'] = "sans-serif"
plt.rc('text', usetex=True)
plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}","\usepackage{xcolor}"]

homeDir = "/home/local/UFAD/rahul.koneru"
baseDir = "/post_processing/NekExamples/so/convergence_AV"
curDir  = "/N200_p4"
rFile   = "/rprof300001"
muFile   = "/muprof300001"
refDir  = "/_output" 
refFile = "/fort.q0010"

refParts = (homeDir, baseDir, refDir, refFile)
ref = np.loadtxt("".join(refParts),skiprows=6)
refParts = (homeDir, baseDir, "/_output_WENO2", refFile)
ref2 = np.loadtxt("".join(refParts),skiprows=6)

# N=200
#curParts = (homeDir, baseDir, curDir,"/profiles/",rFile)
#r_200_p4 = np.loadtxt("".join(curParts))
#
#curParts = (homeDir, baseDir, "/N200_p8" ,"/profiles",rFile)
#r_200_p8 = np.loadtxt("".join(curParts))
#
#curParts = (homeDir, baseDir, "/N200_p16","/profiles",rFile)
#r_200_p16 = np.loadtxt("".join(curParts))
#
#curParts = (homeDir, baseDir, curDir,"/profiles/",muFile)
#mu_200_p4 = np.loadtxt("".join(curParts))
#
#curParts = (homeDir, baseDir, "/N200_p8" ,"/profiles",muFile)
#mu_200_p8 = np.loadtxt("".join(curParts))
#
#curParts = (homeDir, baseDir, "/N200_p16","/profiles",muFile)
#mu_200_p16 = np.loadtxt("".join(curParts))
#
## N=400
#curParts = (homeDir, baseDir, "/N400_p4","/profiles/",rFile)
#r_400_p4 = np.loadtxt("".join(curParts))
#
#curParts = (homeDir, baseDir, "/N400_p8" ,"/profiles",rFile)
#r_400_p8 = np.loadtxt("".join(curParts))
#
#curParts = (homeDir, baseDir, "/N400_p16","/profiles",rFile)
#r_400_p16 = np.loadtxt("".join(curParts))
#
#curParts = (homeDir, baseDir, "/N400_p4","/profiles/",muFile)
#mu_400_p4 = np.loadtxt("".join(curParts))
#
#curParts = (homeDir, baseDir, "/N400_p8" ,"/profiles",muFile)
#mu_400_p8 = np.loadtxt("".join(curParts))
#
#curParts = (homeDir, baseDir, "/N400_p16","/profiles",muFile)
#mu_400_p16 = np.loadtxt("".join(curParts))
#
## N=800
#curParts = (homeDir, baseDir, "/N800_p4","/profiles/",rFile)
#r_800_p4 = np.loadtxt("".join(curParts))
#
#curParts = (homeDir, baseDir, "/N800_p8" ,"/profiles",rFile)
#r_800_p8 = np.loadtxt("".join(curParts))
#
#curParts = (os.getcwd(),"/N800_p16","/profiles",rFile)
#curParts = (os.getcwd(),"/N400_p16","/profiles",rFile)
curParts = (os.getcwd(),"/N200_p16","/profiles",rFile)
r_800_p16 = np.loadtxt("".join(curParts))
#
#curParts = (homeDir, baseDir, "/N800_p4","/profiles/",muFile)
#mu_800_p4 = np.loadtxt("".join(curParts))
#
#curParts = (homeDir, baseDir, "/N800_p8" ,"/profiles",muFile)
#mu_800_p8 = np.loadtxt("".join(curParts))

#curParts = (os.getcwd(), "/N800_p16","/profiles",muFile)
#curParts = (os.getcwd(), "/N400_p16","/profiles",muFile)
curParts = (os.getcwd(), "/N200_p16","/profiles",muFile)
mu_800_p16 = np.loadtxt("".join(curParts))

so_1d_x = np.linspace(-5.0, 5.0, num=20000)

def setGrid(gridIndx):
    ax2.set_title(r'$\mathbf{K=200}$, $\mathbf{p=16}$',fontname="Calibri", fontsize=18)
    ax2.set_xlabel(r'$\mathbf{x}$', fontsize=20)
    ax1.set_ylabel(r'$\boldsymbol{\rho}$', fontsize=20, labelpad=20)
#    ax112.set_ylabel(r'$\boldsymbol{\mu_s,\nu_s,\nu_{max} }$', fontsize=18)
    ax32.set_ylabel(r'$\boldsymbol{ \kappa_s ,\nu_{max} }$', fontsize=20, labelpad=20)
    #ax1.legend(['p=4','p=8','p=12','p=16'], loc='upper right')
#    ax1.grid(True)
#    for tick in ax1.get_xticklabels():
#        tick.set_fontname("Calibri")
#    if gridIndx==0:
##        ax1.set_title("Shock")
#    elif gridIndx==1:
#        ax1.set_xlim(0.66,0.7)
#        ax1.set_ylim(0.25,0.45)
##        ax1.set_title("Contact")
#    elif gridIndx==2:
#        ax1.set_xlim(0.255,0.28)
#        ax1.set_ylim(0.94,1.01)
##        ax1.set_title("Expansion Fan-Head")
#    elif gridIndx==3:
#        ax1.set_xlim(0.475,0.5)
#        ax1.set_ylim(0.42,0.455)
##        ax1.set_title("Expansion Fan-Tail")
	

def saveFig(nameIndx):
    if nameIndx==0:
        plt.savefig('saw-tooth.pdf', dpi=400)
#        plt.savefig('nearshock.pdf', dpi=400)
#        plt.savefig('shuosher-full.pdf', dpi=400)
    elif nameIndx==1:
        plt.savefig('cnt_1Ex.pdf', dpi=400)
    elif nameIndx==2:
        plt.savefig('expH_1Ex.pdf', dpi=400)
    elif nameIndx==3:
        plt.savefig('expT_1Ex.pdf', dpi=400)

def plotSol():
    global lns1,lns2,lns3
    ax1.plot(so_1d_x,ref[:,0],'k', linewidth=2.0)
    ln11 = ax1.plot(r_800_p16[:,0],r_800_p16[:,1],'--r', linewidth=2.0)
    ln12 = ax12.plot(mu_800_p16[:,0],mu_800_p16[:,2],'g', linewidth=2.0)
    ln13 = ax12.plot(mu_800_p16[:,0],mu_800_p16[:,3],'b', linewidth=2.0)
    lns1 = ln11+ln12

    ln21 = ax2.plot(r_800_p16[:,0],r_800_p16[:,1],'--r', linewidth=2.0)
    ln22 = ax22.plot(mu_800_p16[:,0],mu_800_p16[:,2],'g', linewidth=2.0)
    ln23 = ax22.plot(mu_800_p16[:,0],mu_800_p16[:,3],'b', linewidth=2.0)
    ax2.plot(so_1d_x,ref[:,0],'k', linewidth=2.0)
    lns2 = ln11+ln22

    ax3.plot(so_1d_x,ref[:,0],'k', linewidth=2.0)
    ln31 = ax3.plot(r_800_p16[:,0],r_800_p16[:,1],'--r', linewidth=2.0)
    ln32 = ax32.plot(mu_800_p16[:,0],mu_800_p16[:,2],'g', linewidth=2.0)
    ln33 = ax32.plot(mu_800_p16[:,0],mu_800_p16[:,3],'b', linewidth=2.0)
    lns3 = ln31+ln32

#    return lns
#    plt.plot(u_200_p16[:,0],u_200_p16[:,1],'ok',ms=8, fillstyle='none', markevery=15 )
#    plt.plot(re_200_p16[:,0],re_200_p16[:,1],'ok',ms=8, fillstyle='none', markevery=15 )
for i in range(1):
#    plt.figure(i)
#    ax1 = plt.gca()
    plt.clf()
    ax1 = plt.subplot(131)
    ax12= ax1.twinx()
    ax12.ticklabel_format(useOffset=False,style='sci', scilimits=(0,0),axis='y',useMathText=True)
    
    ax2 = plt.subplot(132)
    ax22= ax2.twinx()
    ax22.ticklabel_format(useOffset=False,style='sci', scilimits=(0,0),axis='y',useMathText=True)

    ax3 = plt.subplot(133)
    ax32= ax3.twinx()
    ax32.ticklabel_format(useOffset=False,style='sci', scilimits=(0,0),axis='y',useMathText=True)

    setGrid(i)

#    ln1 = ax1.plot(r_800_p16[:,0],r_800_p16[:,1],'--r', linewidth=2.0)
#    ln2 = ax112.plot(mu_800_p16[:,0],mu_800_p16[:,1],'g', linewidth=2.0)
#    ln3 = ax112.plot(mu_800_p16[:,0],mu_800_p16[:,2],'b', linewidth=2.0)
#    ln4 = ax112.plot(mu_800_p16[:,0],mu_800_p16[:,3],'k', linewidth=1.6)
#    ax112.semilogy(so_1d_x,abs(ref2[:,0]-ref2[:,0]),'.-.k', linewidth=1.2)

    plotSol()

    ax1.set_xlim(0.0,0.5)
#    ax1.set_ylim(3.6,4.2)
    ax1.set_ylim(3.0,5.0)

    ax2.set_xlim(1.2,1.5)
    ax2.set_ylim(3.0,5.0)
    
    ax3.set_xlim(2.20,2.5)
    ax3.set_ylim(3.0,5.0)
 
    y2Shift = 0.0015
    start, end = ax1.get_ylim()
    ax1.yaxis.set_ticks(np.arange(start, end, 0.2))
    ax1.yaxis.set_ticks(np.arange(start, end, 0.5))
    start, end = ax1.get_xlim()
    ax1.xaxis.set_ticks(np.arange(start, end+0.1, 0.1))
    ax1.xaxis.set_ticks(np.arange(start, end+0.1, 0.25))
    start, end = ax12.get_ylim()
    ax12.yaxis.set_ticks(np.arange(start, end, y2Shift))
    ax12.yaxis.set_ticks([])
    ax1.tick_params(labelsize=18)
    ax12.tick_params(labelsize=18)

    start, end = ax2.get_ylim()
    ax2.yaxis.set_ticks(np.arange(start, end+1, 1.0))
    ax2.yaxis.set_ticks([])
    start, end = ax2.get_xlim()
    ax2.xaxis.set_ticks(np.arange(start, end, 0.1))
    start, end = ax12.get_ylim()
    ax22.yaxis.set_ticks(np.arange(start, end, y2Shift))
    ax22.yaxis.set_ticks([])
    ax2.tick_params(labelsize=18)
    ax22.tick_params(labelsize=18)

    start, end = ax3.get_ylim()
    ax3.yaxis.set_ticks(np.arange(start, end+1, 1.0))
    ax3.yaxis.set_ticks([])
    start, end = ax3.get_xlim()
    ax3.xaxis.set_ticks(np.arange(start, end+0.1, 0.1))
    start, end = ax12.get_ylim()
    ax32.yaxis.set_ticks(np.arange(start, end, y2Shift))
    ax3.tick_params(labelsize=18)
    ax32.tick_params(labelsize=18)

#    ax1.legend(lns1,[r'$\rho$',r'$\mu_s$',r'$\nu_s$',r'$R_s$'], loc='upper right')
#    saveFig(i)
#plt.pause(0.1)    
plt.show()
#plt.show(block=False)
