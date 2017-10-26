#!/usr/bin/python

import sys
import matplotlib.pyplot as plt
import numpy as np

plt.rc('text', usetex=True)
plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

#N = [200,400,800,1600]
N = [200,400,800]
p = range(4,14,2)
p = [4,8,16] 
#print p
baseDir = "/home/local/UFAD/rahul.koneru/post_processing/NekExamples/so/convergence_AV"
refDir = "/_output"
refFile = "/fort.q0010"
refParts = (baseDir, refDir, refFile)
#print "".join(refParts)
rhoFile = "/rprof300001"
syms = ['k^','ks','ok']
ref_x = np.linspace(-5.0, 5.0, num=20000)

#ref = np.loadtxt('/home/local/UFAD/rahul.koneru/post_processing/NekExamples/so/convergence/_output/fort.q0010', skiprows=6)
#N200_p4 = np.loadtxt('/home/local/UFAD/rahul.koneru/post_processing/NekExamples/so/convergence/N200_p4/rprof100000')
#N400_p4 = np.loadtxt('/home/local/UFAD/rahul.koneru/post_processing/NekExamples/so/convergence/N400_p4/rprof100000')
#N800_p4 = np.loadtxt('/home/local/UFAD/rahul.koneru/post_processing/NekExamples/so/convergence/N800_p4/rprof100000')
#
#
#i_N200_p4 = np.interp(N200_p4[:,0],ref_x,ref[:,0])
#i_N400_p4 = np.interp(N400_p4[:,0],ref_x,ref[:,0])
#i_N800_p4 = np.interp(N800_p4[:,0],ref_x,ref[:,0])
#
#l1_N200_p4 = np.linalg.norm(i_N200_p4-N200_p4[:,1],ord=1)
#l1_N400_p4 = np.linalg.norm(i_N400_p4-N400_p4[:,1],ord=1)
#l1_N800_p4 = np.linalg.norm(i_N800_p4-N800_p4[:,1],ord=1)
#
#l1_N200 = sum(abs(i_N200_p4-N200_p4[:,1]))/len(i_N200_p4)
#l1_N400 = sum(abs(i_N400_p4-N400_p4[:,1]))/len(i_N400_p4)
#l1_N800 = sum(abs(i_N800_p4-N800_p4[:,1]))/len(i_N800_p4)
#
##print l1_N200_p4, l1_N400_p4, l1_N800_p4
#print l1_N200, l1_N400, l1_N800

ref = np.loadtxt("".join(refParts), skiprows=6)
count = 0
l = 0
arr_err_l1 = np.zeros((len(N),len(p)))
#arr_err[0] = 1
#print arr_err[0]
#plt.ion()
#plt.show()

for indxp, i in enumerate(p):
#    print i
    leg = 1
    for indxN, j in enumerate(N):
#        print j
        currFolderParts = ("/N",str(j),"_p",str(i))
        currFolder = "".join(currFolderParts)
#        print currFolder
        currFileParts = (baseDir,currFolder,"/profiles",rhoFile)
        fileNP = np.loadtxt("".join(currFileParts))

        i_fileNP = np.interp(fileNP[:,0],ref_x,ref[:,0])
        
        err = np.divide(i_fileNP-fileNP[:,1],i_fileNP)
        err = np.divide( abs(i_fileNP-fileNP[:,1]),abs(i_fileNP) )
#        err = i_fileNP-fileNP[:,1]
#        err = err/len(i_fileNP)
        l1   = np.linalg.norm(err,ord=1)/len(i_fileNP)
        linf = max(err)
#        print currFolder
        print('N=%s, p=%s, L1=%5.3E, Linf=%5.3E' % (str(j),str(i),l1,linf) )
        arr_err_l1[indxN,indxp] = l1

        if indxN > 0:
            m = (np.log(arr_err_l1[indxN,indxp])-np.log(arr_err_l1[indxN-1,indxp]))/(np.log(1.0/j/2)-np.log(1.0/j))
            print ('m=%5.4f' % m)

        l = l+1
#        plt.loglog(1.0/j,l1,'k^')
        plt.loglog(1.0/j,l1,syms[count], ms=8, label=r'$p = $ %i' % i if leg==1 else "")
        leg = 0

    count = count+1
#print arr_err[0:3]
    slope, intercept = np.polyfit(np.log(np.divide(1.0,N)), np.log(arr_err_l1[:,indxp]), 1 )
    print ('m_fit=%4.3f, int=%4.3f' % (slope,intercept))
#    print slope

#plt.xticks((10**-4,10**-3,10**-2),(r'$10^{-4}$',r'$10^{-3}$',r'$10^{-2}$'),weight='extra bold')
#plt.axis([1e-3,1e-2,1e-4,1e-1])
plt.legend()
plt.xlabel(r'$h$', fontsize=18)
plt.ylabel(r'$E_{L1}$', fontsize=18)
figTitle = '/conv_v2.png'
figParts = (baseDir,figTitle)
#plt.savefig(''.join(figParts))
#plt.savefig('so_conv.png')
#plt.draw()
#plt.ion()
#plt.pause(5.0)
#plt.show()


#        l1_fileNP = np.linalg.norm(i_fileNP-fileNP[:,1],ord=1)
#print intrp.shape
#print len(intrp)
#print len(N200_p4)
#print intrp
#print sys.argv[0],sys.argv[1]

#if sys.argv[1] == '1':
#    #plt.plot(N200_p4[:,0],N200_p4[:,1],'o-r', linewidth=2.0)
#    #plt.plot(N400_p4[:,0],N400_p4[:,1],'o-k', linewidth=2.0)
#    #plt.plot(N800_p4[:,0],N800_p4[:,1],'o-g', linewidth=2.0)
#    #plt.plot(ref_x,ref[:,0],'b', linewidth=2.0)
#    #plt.plot(N200_p4[:,0],i_N200_p4,'-k', linewidth=2.0)
#    plt.loglog([0.05,0.025,0.0125],[l1_N200,l1_N400,l1_N800])
#    plt.legend(['CMT-Nek','Clawpack'], loc='upper right')
#    #plt.xlim(-4.0,3.0)
#    #plt.xlim(-1.945,-1.925)
#    plt.title(r'$t=1.8s$')
#    plt.xlabel(r'$x (m)$', fontsize=18)
#    plt.ylabel(r'$\boldsymbol{\rho (kg/m^3)}$', fontsize=18)
#    plt.grid(True)
#    #plt.savefig('rho_cmt-claw.png')
#    plt.show()
#else:
#    print
