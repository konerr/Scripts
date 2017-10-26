#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

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

curParts = (homeDir, baseDir, curDir,"/profiles/rprof001000")
r1av_200_p4 = np.loadtxt("".join(curParts))

curParts = (homeDir, baseDir, curDir,"/profiles/rprof003000")
r3av_200_p4 = np.loadtxt("".join(curParts))

curParts = (homeDir, baseDir, curDir,"/profiles/rprof005000")
r5av_200_p4 = np.loadtxt("".join(curParts))

so_1d_x = np.linspace(-5.0, 5.0, num=20000)

plt.clf()
plt.figure(1)
plt.subplot(311)
plt.plot(r1_200_p4[:,0],r1_200_p4[:,1],'o-r', linewidth=2.0)
plt.plot(r1av_200_p4[:,0],r1av_200_p4[:,1],'o-b', linewidth=2.0)
plt.plot(r1_200_p4[:,0],r1_200_p4[:,2],'k', linewidth=2.0)

plt.legend(['CMT-Nek','AV','Exact'], loc='upper right')
plt.title('t=1.8s')
plt.xlim(0.4,0.6)
#plt.xlabel('x', fontsize=18)
#plt.ylabel(r'$\boldsymbol{\rho (kg/m^3)}$', fontsize=18)
plt.ylabel(r'$\boldsymbol{\rho}$', fontsize=18)
plt.grid(True)

plt.subplot(312)
plt.plot(r3_200_p4[:,0],r3_200_p4[:,1],'o-r', linewidth=2.0)
plt.plot(r3av_200_p4[:,0],r3av_200_p4[:,1],'o-b', linewidth=2.0)
plt.plot(r3_200_p4[:,0],r3_200_p4[:,2],'k', linewidth=2.0)

plt.legend(['CMT-Nek','Exact'], loc='upper right')
plt.title('t=1.8s')
plt.xlim(0.3,0.8)
#plt.xlabel('x', fontsize=18)
#plt.ylabel(r'$\boldsymbol{\rho (kg/m^3)}$', fontsize=18)
plt.ylabel(r'$\boldsymbol{\rho}$', fontsize=18)
plt.grid(True)

plt.subplot(313)
plt.plot(r5_200_p4[:,0],r5_200_p4[:,1],'o-r', linewidth=2.0)
plt.plot(r5av_200_p4[:,0],r5av_200_p4[:,1],'o-b', linewidth=2.0)
plt.plot(r5_200_p4[:,0],r5_200_p4[:,2],'k', linewidth=2.0)

plt.legend(['CMT-Nek','Exact'], loc='upper right')
plt.title('t=1.8s')
plt.xlim(0.2,0.9)
plt.xlabel('x', fontsize=18)
#plt.ylabel(r'$\boldsymbol{\rho (kg/m^3)}$', fontsize=18)
plt.ylabel(r'$\boldsymbol{\rho}$', fontsize=18)
plt.grid(True)

#plt.savefig('rho_cmt-claw.png')
plt.show()
