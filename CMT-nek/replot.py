#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

#plt.ion()
plt.rc('text', usetex=True)
plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

homeDir = "/home/local/UFAD/rahul.koneru"
baseDir = "/post_processing/NekExamples/sod3_ALL/convergence"
curDir = "/N200_p4"
refFile = "/fort.q0010"

curParts = (homeDir, baseDir, curDir,"/profiles_oldvisc/rprof001000")
r1_200_p4 = np.loadtxt("".join(curParts))

curParts = (homeDir, baseDir, curDir,"/profiles_oldvisc/rprof002000")
r2_200_p4 = np.loadtxt("".join(curParts))

curParts = (homeDir, baseDir, curDir,"/profiles_oldvisc/rprof003000")
r3_200_p4 = np.loadtxt("".join(curParts))

curParts = (homeDir, baseDir, curDir,"/profiles_oldvisc/rprof004000")
r4_200_p4 = np.loadtxt("".join(curParts))

curParts = (homeDir, baseDir, curDir,"/profiles_oldvisc/rprof005000")
r5_200_p4 = np.loadtxt("".join(curParts))

# N=200
curParts = (homeDir, baseDir, curDir,"/profiles/rprof020001")
r_200_p4 = np.loadtxt("".join(curParts))

curParts = (homeDir, baseDir, "/N200_p8" ,"/profiles/rprof020001")
r_200_p8 = np.loadtxt("".join(curParts))

curParts = (homeDir, baseDir, "/N200_p12","/profiles/rprof020001")
r_200_p12 = np.loadtxt("".join(curParts))

curParts = (homeDir, baseDir, "/N200_p16","/profiles/rprof020001")
r_200_p16 = np.loadtxt("".join(curParts))

curParts = (homeDir, baseDir, "/N200_p16","/profiles/uprof040001")
u_200_p16 = np.loadtxt("".join(curParts))

curParts = (homeDir, baseDir, "/N200_p16","/profiles/reprof040001")
re_200_p16 = np.loadtxt("".join(curParts))

curParts = (homeDir, baseDir, "/N200_p16","/profiles/Tprof040001")
T_200_p16 = np.loadtxt("".join(curParts))

# N=100
curParts = (homeDir, baseDir, "/N100_p4" ,"/profiles/rprof020001")
r_100_p4 = np.loadtxt("".join(curParts))

curParts = (homeDir, baseDir, "/N100_p8","/profiles/rprof020001")
r_100_p8 = np.loadtxt("".join(curParts))

curParts = (homeDir, baseDir, "/N100_p12","/profiles/rprof020001")
r_100_p12 = np.loadtxt("".join(curParts))

curParts = (homeDir, baseDir, "/N100_p16","/profiles/rprof020001")
r_100_p16 = np.loadtxt("".join(curParts))

# N=50
curParts = (homeDir, baseDir, "/N50_p4" ,"/profiles/rprof020001")
r_50_p4 = np.loadtxt("".join(curParts))

curParts = (homeDir, baseDir, "/N50_p8" ,"/profiles/rprof020001")
r_50_p8 = np.loadtxt("".join(curParts))

curParts = (homeDir, baseDir, "/N50_p12" ,"/profiles/rprof020001")
r_50_p12 = np.loadtxt("".join(curParts))

curParts = (homeDir, baseDir, "/N50_p16" ,"/profiles/rprof020001")
r_50_p16 = np.loadtxt("".join(curParts))

so_1d_x = np.linspace(-5.0, 5.0, num=20000)

def setGrid(gridIndx):
    ax.set_xlabel(r'$\mathbf{x}$', fontsize=18)
    ax.set_ylabel(r'$\boldsymbol{\rho}$', fontsize=18)
    ax.legend(['p=4','p=8','p=12','p=16'], loc='upper right')
    ax.grid(True)

    if gridIndx==0:
        ax.set_xlim(0.844,0.856)
        ax.set_ylim(0.12,0.28)
#        ax.set_title("Shock")
    elif gridIndx==1:
        ax.set_xlim(0.66,0.7)
        ax.set_ylim(0.25,0.45)
#        ax.set_title("Contact")
    elif gridIndx==2:
        ax.set_xlim(0.255,0.28)
        ax.set_ylim(0.94,1.01)
#        ax.set_title("Expansion Fan-Head")
    elif gridIndx==3:
        ax.set_xlim(0.475,0.5)
        ax.set_ylim(0.42,0.455)
#        ax.set_title("Expansion Fan-Tail")


def saveFig(nameIndx):
    if nameIndx==0:
        plt.savefig('shock_1Ex.pdf', dpi=400)
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
#    plt.plot(r_200_p16[:,0],r_200_p16[:,1],'o-k', linewidth=2.0)

#    plt.plot(r_200_p4[:,0], r_200_p4[:,1],'r', linewidth=2.0)
#    plt.plot(r_200_p8[:,0], r_200_p8[:,1],'b', linewidth=2.0)
#    plt.plot(r_200_p12[:,0],r_200_p12[:,1],'g', linewidth=2.0)
#    plt.plot(r_200_p16[:,0],r_200_p16[:,1],'k', linewidth=2.0)

#    plt.plot(r_50_p8[:,0], r_50_p8[:,1],'r', linewidth=2.0)
#    plt.plot(r_100_p8[:,0], r_100_p8[:,1],'b', linewidth=2.0)
#    plt.plot(r_200_p8[:,0],r_200_p8[:,1],'g', linewidth=2.0)
#    plt.plot(r_200_p16[:,0],r_200_p16[:,1],'k', linewidth=2.0)

    plt.plot(u_200_p16[:,0],u_200_p16[:,1],'ok',ms=8, fillstyle='none', markevery=15 )
#    plt.plot(re_200_p16[:,0],re_200_p16[:,1],'ok',ms=8, fillstyle='none', markevery=15 )
for i in range(4):
#    plt.figure(i)
    plt.clf()
    plotSol()
    ax = plt.gca()

#    setGrid(i)

# Exact solution
#    plt.plot(r_200_p16[:,0],r_200_p16[:,2],'--k', linewidth=2.0)
    plt.plot(u_200_p16[:,0],u_200_p16[:,2],'k', linewidth=2.0)
#    plt.plot(re_200_p16[:,0],re_200_p16[:,2],'k', linewidth=2.0)

    #saveFig(i)
#plt.pause(0.1)    
plt.show()
#plt.show(block=False)
