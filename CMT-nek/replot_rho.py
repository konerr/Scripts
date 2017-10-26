#!/usr/bin/python

import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import numpy as np

#plt.ion()
plt.rc('text', usetex=True)
plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

homeDir = "/home/local/UFAD/rahul.koneru"
baseDir = "/post_processing/NekExamples/so/convergence_AV"
curDir  = "/N200_p4"
rFile   = "/rprof300001"
refDir  = "/_output" 
refFile = "/fort.q0010"

refParts = (homeDir, baseDir, refDir, refFile)
ref = np.loadtxt("".join(refParts),skiprows=6)
refParts = (homeDir, baseDir, "/_output_WENO2", refFile)
ref2 = np.loadtxt("".join(refParts),skiprows=6)

# N=200
curParts = (homeDir, baseDir, curDir,"/profiles/",rFile)
r_200_p4 = np.loadtxt("".join(curParts))

curParts = (homeDir, baseDir, "/N200_p8" ,"/profiles",rFile)
r_200_p8 = np.loadtxt("".join(curParts))

curParts = (homeDir, baseDir, "/N200_p16","/profiles",rFile)
r_200_p16 = np.loadtxt("".join(curParts))

# N=400
curParts = (homeDir, baseDir, "/N400_p4","/profiles/",rFile)
r_400_p4 = np.loadtxt("".join(curParts))

curParts = (homeDir, baseDir, "/N400_p8" ,"/profiles",rFile)
r_400_p8 = np.loadtxt("".join(curParts))

curParts = (homeDir, baseDir, "/N400_p16","/profiles",rFile)
r_400_p16 = np.loadtxt("".join(curParts))

# N=800
curParts = (homeDir, baseDir, "/N800_p4","/profiles/",rFile)
r_800_p4 = np.loadtxt("".join(curParts))

curParts = (homeDir, baseDir, "/N800_p8" ,"/profiles",rFile)
r_800_p8 = np.loadtxt("".join(curParts))

curParts = (homeDir, baseDir, "/N800_p16","/profiles",rFile)
r_800_p16 = np.loadtxt("".join(curParts))

so_1d_x = np.linspace(-5.0, 5.0, num=20000)

def setGrid(gridIndx):
    ax.set_xlabel(r'$\mathbf{x}$', fontsize=18)
    ax.set_ylabel(r'$\boldsymbol{\rho}$', fontsize=18)
    #ax.legend(['p=4','p=8','p=12','p=16'], loc='upper right')
#    ax.grid(True)

    if gridIndx==0:
        ax.set_xlim(-2.0,0.0)
        ax.set_ylim(3.50,4.25)
#        ax.set_xlim( 0.5,2.5)
#        ax.set_ylim(3.00,5.00)
#        ax.set_xlim(-5.0,5.0)
#       ax.set_ylim(3.00,5.00)
##        ax.set_title("Shock")
#    elif gridIndx==1:
#        ax.set_xlim(0.66,0.7)
#        ax.set_ylim(0.25,0.45)
##        ax.set_title("Contact")
#    elif gridIndx==2:
#        ax.set_xlim(0.255,0.28)
#        ax.set_ylim(0.94,1.01)
##        ax.set_title("Expansion Fan-Head")
#    elif gridIndx==3:
#        ax.set_xlim(0.475,0.5)
#        ax.set_ylim(0.42,0.455)
##        ax.set_title("Expansion Fan-Tail")
	

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
#    plt.plot(r_200_p4[:,0], r_200_p4[:,1],'o-r', linewidth=2.0)
#    plt.plot(r_200_p8[:,0], r_200_p8[:,1],'o-b', linewidth=2.0)
#    plt.plot(r_200_p12[:,0],r_200_p12[:,1],'o-g', linewidth=2.0)
    plt.plot(r_200_p16[:,0],r_200_p16[:,1],'o-k', linewidth=2.0)
    ax.plot(r_800_p16[:,0],r_800_p16[:,1],'--r', linewidth=2.0)
#    plt.plot(r_800_p16[:,0],r_800_p16[:,1],'or', ms=8.0, markevery=10)

#    plt.plot(r_200_p4[:,0], r_200_p4[:,1],'r', linewidth=2.0)
#    plt.plot(r_200_p8[:,0], r_200_p8[:,1],'b', linewidth=2.0)
#    plt.plot(r_200_p12[:,0],r_200_p12[:,1],'g', linewidth=2.0)
#    plt.plot(r_200_p16[:,0],r_200_p16[:,1],'k', linewidth=2.0)

#    plt.plot(r_50_p8[:,0], r_50_p8[:,1],'r', linewidth=2.0)
#    plt.plot(r_100_p8[:,0], r_100_p8[:,1],'b', linewidth=2.0)
#    plt.plot(r_200_p8[:,0],r_200_p8[:,1],'g', linewidth=2.0)
#    plt.plot(r_200_p16[:,0],r_200_p16[:,1],'k', linewidth=2.0)

#    plt.plot(u_200_p16[:,0],u_200_p16[:,1],'ok',ms=8, fillstyle='none', markevery=15 )
#    plt.plot(re_200_p16[:,0],re_200_p16[:,1],'ok',ms=8, fillstyle='none', markevery=15 )
for i in range(1):
#    plt.figure(i)
    plt.clf()
    ax = plt.gca()
    ax2= ax.twinx()
    i_fileNP = np.interp(r_800_p16[:,0],so_1d_x,ref[:,0])
    i_fileNP2 = np.interp(r_800_p16[:,0],so_1d_x,ref2[:,0])
    err = abs(i_fileNP-r_800_p16[:,1])
    err2 = abs(i_fileNP2-r_800_p16[:,1])
    x = np.linspace(-5.0, 5.0, num=len(err))
#    print len(i_fileNP),len(err), len(r_800_p16)
#    setGrid(i)

# Exact solution
#    plt.plot(r_800_p16[:,0],i_fileNP,'or')
#    plt.plot(so_1d_x,ref[:,0],'k', linewidth=1.2)
    ax.plot(so_1d_x,ref[:,0],'b', linewidth=1.2)
#    ax.plot(so_1d_x,ref2[:,0],'k', linewidth=1.2)
#    ax2.semilogy(so_1d_x,abs(ref2[:,0]-ref2[:,0]),'.-.k', linewidth=1.2)
#    ax.plot(x,i_fileNP,'k', linewidth=1.2)
#    ax2.semilogy(x,err,'.-.b', linewidth=1.2)
#    ax2.semilogy(x,err2,'.-.k', linewidth=1.2)
#    plt.plot(re_200_p16[:,0],re_200_p16[:,2],'k', linewidth=2.0)

    plotSol()
    ax.set_xlim(-5.0,5.0)
    ax.legend(['N=800,p=16','Exact'], loc='upper right')
#    saveFig(i)
#plt.pause(0.1)    
plt.show()
#plt.show(block=False)
