#!/usr/bin/python
# Sod3 hp convergence

import sys
import matplotlib.pyplot as plt
import numpy as np

plt.rc('text', usetex=True)
plt.rc('font', weight='bold')
plt.rc('axes', linewidth=1.4)
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

plt.rc('xtick', labelsize=14)
plt.rc('xtick.major', size=10, pad=8)
plt.rc('xtick.minor', size=6)
plt.rc('ytick', labelsize=14)
plt.rc('ytick.major', size=10)
plt.rc('ytick.minor', size=6)

N = [50, 100, 200]
p = [4, 8, 12, 16]
#p = [4, 8, 16]
#p = range(4,8,4)

baseDir = "/home/local/UFAD/rahul.koneru/post_processing/NekExamples/sod3_ALL/convergence"
rhoFile = "/rprof020001"
refDir = "/N200_p16/profiles"
refFile = rhoFile 
refParts = (baseDir, refDir, refFile)

syms = ['k^','ks','ok','>k']
syms2 = ['r^','rs','or','>r']
syms3 = ['b^','bs','ob']

ref_x = np.linspace(-5.0, 5.0, num=20000)
ref = np.loadtxt("".join(refParts))

count = 0
l = 0
#arr_err_l1   = np.zeros((len(N)*len(p)))
arr_err_l1   = np.zeros((len(N),len(p)))
arr_err_l2   = np.zeros((len(N)*len(p)))
arr_err_linf = np.zeros((len(N)*len(p)))
theta        = np.zeros((len(p)))

for indxp, i in enumerate(p):
    leg = 1
    for indxN, j in enumerate(N):
        currFolderParts = ("/N",str(j),"_p",str(i),"/profiles")
        currFolder = "".join(currFolderParts)
        currFileParts = (baseDir,currFolder,rhoFile)
        fileNP = np.loadtxt("".join(currFileParts))

        
#        err = np.divide(fileNP[:,2]-fileNP[:,1],fileNP[:,2])
        err = np.divide( abs(fileNP[:,2]-fileNP[:,1]),abs(fileNP[:,2]) )
#        err = i_fileNP-fileNP[:,1]
#        err = err/len(i_fileNP)
        l1  = np.linalg.norm(err,ord=1)/len(fileNP[:,2])
        l2  = np.linalg.norm(err,ord=2)/len(fileNP[:,2])
        linf= max(err)
#
        iref = np.interp(fileNP[:,0],ref[:,0],ref[:,2])
        err = np.divide( abs(iref-fileNP[:,1]),abs(iref) )
        l1  = np.linalg.norm(err,ord=1)/len(iref)
        l2  = np.linalg.norm(err,ord=2)/len(iref)
        linf= max(err)
        print('N=%s, p=%s, L1=%5.3E, L2=%5.3E, Linf=%5.3E' % (str(j),str(i),l1,l2,linf) )
        arr_err_l1[indxN,indxp]   = l1
        arr_err_l2[l]   = l2
        arr_err_linf[l] = linf
        
        if indxN > 0:
            m = (np.log(arr_err_l1[indxN,indxp])-np.log(arr_err_l1[indxN-1,indxp]))/(np.log(1.0/j/2)-np.log(1.0/j))
            print ('m=%5.4f' % m)
        l = l+1

        fig1 = plt.figure(1)
        ax1 = fig1.add_subplot(1,1,1)
        ax1.loglog(1.0/j,l1,syms[count], ms=8, label=r'$p = $ %i' % i if leg==1 else "")

        leg = 0

    count = count+1
#    slope, intercept = np.polyfit(np.log(np.divide(1.0,N)), np.log(arr_err_l1[0:len(N)]), 1 )
    slope, intercept = np.polyfit(np.log(np.divide(1.0,N)), np.log(arr_err_l1[:,indxp]), 1 )
#    theta[indxp] = np.arctan2( np.log(arr_err_l1[:,indxp]), np.log(np.divide(1.0,N)) )
    theta[indxp] = np.rad2deg(np.arctan(slope))
#    print theta, 
#    print arr_err_l1[indxN,:]
#    print arr_err_l1[:,indxp]
 #   y_fit = [slope * i + intercept for i in p]
    y_fit = [slope * np.log(1.0/j) + intercept for j in N]
#    y_fit = [slope * 1.0/j + intercept for j in N]
#    print y_fit,np.exp(y_fit)
    y_fit = np.exp(y_fit)
    ax1.loglog(np.divide(1.0,N),y_fit,'k--', ms=8)
    print ('m_fit=%4.3f, int=%4.3f' % (slope,intercept))
#print theta

#fig1.set_size_inches(8,6)
ax1.legend()
ax1.text(0.013,0.020, r'$\Huge{h^{0.910}}$',rotation=theta[0], fontsize=12)
ax1.text(0.013,0.011, r'$\Huge{h^{0.846}}$',rotation=theta[1],fontsize=12)
#ax1.text(0.013,0.0070, r'$\Huge{h^{0.755}}$',rotation=theta[2],fontsize=12)
ax1.text(0.013,0.006, r'$\Huge{h^{0.709}}$',rotation=theta[2],fontsize=12)
ax1.set_xlabel(r'$h$', fontsize=16)
ax1.set_ylabel(r'$E_{L_{1}}$', fontsize=16)
#ax1.tick_params(length=12,width=1.2,which="major")
#ax1.tick_params(length=7,width=1.2,which="minor")
#plt.show()
#ax2.legend()
#ax2.set_xlabel(r'$h$', fontsize=14)
#ax2.set_ylabel(r'$E_{L2}$', fontsize=14)

#ax4.legend()
#ax4.set_xlabel(r'$h$', fontsize=14)
#ax4.set_ylabel(r'$E_{L2}$', fontsize=14)
#plt.close(fig2)

figTitle = '/sod3_NL1_h.pdf'
figParts = (baseDir,figTitle)
#plt.savefig(''.join(figParts))
#plt.savefig(''.join(figParts), bbox_inches='tight')
#plt.savefig(''.join(figParts), dpi=400, bbox_inches='tight')
#plt.savefig('conv_v1.png')
#plt.draw()
#plt.ion()
#plt.pause(5.0)
#plt.show()

count = 0
l = 0
for indxN, j in enumerate(N):
    leg = 1
    for indxp, i in enumerate(p):
        currFolderParts = ("/N",str(j),"_p",str(i),"/profiles")
        currFolder = "".join(currFolderParts)
#        print currFolder
        currFileParts = (baseDir,currFolder,rhoFile)
        fileNP = np.loadtxt("".join(currFileParts))

#        i_fileNP = np.interp(fileNP[:,0],ref_x,ref[:,0])
        
#        err = np.divide(fileNP[:,2]-fileNP[:,1],fileNP[:,2])
        err = np.divide( abs(fileNP[:,2]-fileNP[:,1]),abs(fileNP[:,2]) )
#        err = i_fileNP-fileNP[:,1]
#        err = err/len(i_fileNP)
        l1  = np.linalg.norm(err,ord=1)/len(fileNP[:,2])
        l2  = np.linalg.norm(err,ord=2)/len(fileNP[:,2])
        linf= max(err)
#        print currFolder
#        print('N=%s, p=%s, L1=%5.3E, L2=%5.3E, Linf=%5.3E' % (str(j),str(i),l1,l2,linf) )
        arr_err_l1[indxN,indxp]   = l1
#        arr_err_l2[l]   = l2
#        arr_err_linf[l] = linf
        
#        if indxp > 0:
#            m = (np.log(arr_err_l1[indxN,indxp])-np.log(arr_err_l1[indxN,indxp-1]))/(i-i/2)
#            print ('m=%5.4f' % m)
        l = l+1

        fig2 = plt.figure(2)
        ax2 = fig2.add_subplot(1,1,1)
        ax2.semilogy(i,l1,syms[count], ms=8, label=r'$N = $ %i' % j if leg==1 else "")

        leg = 0

    count = count+1
    slope, intercept = np.polyfit(p, np.log(arr_err_l1[indxN,:]), 1 )
    y_fit = [slope * i + intercept for i in p]
    y_fit = np.exp(y_fit)
    ax2.semilogy(p,y_fit,'k--', ms=8)
#    print ('m_fit=%4.3f, int=%4.3f' % (slope,intercept))

ax2.legend()
ax2.text(5,0.021, r'$m=-0.105$',rotation=-13, fontsize=12)
ax2.text(5,0.011, r'$m=-0.083$',rotation=-11,fontsize=12)
ax2.text(5,0.006, r'$m=-0.081$',rotation=-12,fontsize=12)
ax2.set_xlim([3, 17])
ax2.set_xlabel(r'$p$', fontsize=14)
ax2.set_ylabel(r'$E_{L1}$', fontsize=14)

figTitle = '/sod3_pL1_v2.pdf'
figParts = (baseDir,figTitle)
#plt.savefig(''.join(figParts), dpi=400, bbox_inches='tight')
#plt.pause(5.0)
#plt.show()
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
