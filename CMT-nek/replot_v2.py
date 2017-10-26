#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

plt.rc('text', usetex=True)
plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

def setGrid():
    ax1.set_xlabel(r'$x$', fontsize=18)
    ax1.set_ylabel(r'$\boldsymbol{\rho}$', fontsize=18)
    ax2.set_xlabel(r'$x$', fontsize=18)
    ax2.set_ylabel(r'$\boldsymbol{\rho}$', fontsize=18)
    ax3.set_xlabel(r'$x$', fontsize=18)
    ax3.set_ylabel(r'$\boldsymbol{\rho}$', fontsize=18)
    ax4.set_xlabel(r'$x$', fontsize=18)
    ax4.set_ylabel(r'$\boldsymbol{\rho}$', fontsize=18)

    ax1.grid(True)
    ax2.grid(True)
    ax3.grid(True)
    ax4.grid(True)

def setGrid():
    ax.set_xlabel(r'$x$', fontsize=18)
    ax.set_ylabel(r'$\boldsymbol{\rho}$', fontsize=18)

    ax.legend()
    ax.grid(True)


homeDir = "/home/local/UFAD/rahul.koneru"
baseDir = "/post_processing/NekExamples/sod3_ALL/convergence"
curDir = "/N200_p4"
refFile = "/fort.q0010"

curParts = (homeDir, baseDir, curDir,"/profiles/rprof020001")
r_200_p4 = np.loadtxt("".join(curParts))

curParts = (homeDir, baseDir, "/N200_p8" ,"/profiles/rprof020001")
r_200_p8 = np.loadtxt("".join(curParts))

curParts = (homeDir, baseDir, "/N200_p12","/profiles/rprof020001")
r_200_p12 = np.loadtxt("".join(curParts))

curParts = (homeDir, baseDir, "/N200_p16","/profiles/rprof020001")
r_200_p16 = np.loadtxt("".join(curParts))

so_1d_x = np.linspace(-5.0, 5.0, num=20000)
#r_200 = np.dstack((r_200_p4,r_200_p8,r_200_p12,r_200_p16))
#r_200 = np.dstack((r_200_p4,r_200_p4))
#print r_200.shape

fig2, axes = plt.subplots(nrows=2,ncols=2)
for i, ax in enumerate(axes.flatten()):
    ax.plot(r_200_p4[:,0], r_200_p4[:,1],'r', linewidth=2.0)
    ax.plot(r_200_p8[:,0], r_200_p8[:,1],'b', linewidth=2.0)
#    ax.plot(r_200_p12[:,0],r_200_p12[:,1],'o-g', linewidth=2.0)
    ax.plot(r_200_p16[:,0],r_200_p16[:,1],'g', linewidth=2.0)
    setGrid() 
    
    if i==0:
        ax.set_xlim(0.844,0.856)
        ax.set_ylim(0.12,0.28)
        ax.set_title("Shock")
    elif i==1:
        ax.set_xlim(0.66,0.7)
        ax.set_ylim(0.25,0.45)
        ax.set_title("Contact")
    elif i==2:
        ax.set_xlim(0.255,0.28)
        ax.set_ylim(0.94,1.01)
        ax.set_title("Expansion Fan-Head")
    elif i==3:
        ax.set_xlim(0.475,0.5)
        ax.set_ylim(0.42,0.455)
        ax.set_title("Expansion Fan-Tail")
    
    ax.plot(r_200_p16[:,0],r_200_p16[:,2],'--k', linewidth=2.0)
#fig1 = plt.figure(1)
#ax1 = fig1.add_subplot(221)
#ax1 = fig1.add_subplot(222)
#ax1 = fig1.add_subplot(223)
#ax1 = fig1.add_subplot(224)
#plt.plot(r_200_p4[:,0], r_200_p4[:,2],'r', linewidth=2.0)
#plt.plot(r_200_p8[:,0], r_200_p8[:,2],'b', linewidth=2.0)
#plt.plot(r_200_p12[:,0],r_200_p12[:,2],'g', linewidth=2.0)

#ax1.plot(r_200_p4[:,0], r_200_p4[:,1],'o-r', linewidth=2.0)
#ax1.plot(r_200_p8[:,0], r_200_p8[:,1],'o-b', linewidth=2.0)
#ax1.plot(r_200_p12[:,0],r_200_p12[:,1],'o-g', linewidth=2.0)
#ax1.plot(r_200_p16[:,0],r_200_p16[:,1],'o-k', linewidth=2.0)
#setGrid()

#ax1.legend(['p=4','p=8','p=12','p=16'], loc='upper right')
#plt.title(r'$t=0.2s$')
#plt.xlim(0.8490,0.8510)
#plt.ylim(0.12,0.27)

#ax1.plot(r_200_p16[:,0],r_200_p16[:,2],'--k', linewidth=2.0)

#plt.xlim(0.678,0.690)

#ax3.set_xlim(0.255,0.280)
#ax3.set_ylim(0.94,1.01)

#ax4.set_xlim(0.475,0.5)
#ax4.set_ylim(0.42,0.455)

#plt.savefig('shock_allEx.png')
#plt.savefig('cnt_1Ex.png')
#plt.savefig('cnt_1Ex.pdf', dpi=400)
#plt.savefig('shock_1Ex.pdf', dpi=400)
#plt.savefig('expH_1Ex.pdf', dpi=400)
#plt.savefig('expT_1Ex.pdf', dpi=400)
#plt.savefig('all.pdf', dpi=400)
plt.show()
