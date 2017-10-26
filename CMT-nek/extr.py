#!/usr/bin/python

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

# File Name : kap_p.py

# Purpose : Extract CFL, Diff#, Knd and
# \kappa_s. Average them and write to a file

# Created By : Rahul Koneru 

#_._._._._._._._._._._._._._._._._._._._._.


import sys
import matplotlib.pyplot as plt
import numpy as np

plt.rc('text', usetex=True)
plt.rc('font', weight='bold')
#plt.rc('axes', linewidth=2)
plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

plt.rc('xtick', labelsize=14)
plt.rc('xtick.major', size=10, pad=8)
plt.rc('xtick.minor', size=5)
plt.rc('ytick', labelsize=14)
plt.rc('ytick.major', size=10)
plt.rc('ytick.minor', size=5)

N = [50, 100, 200]
#N = [100,200]
p = [4,8,12,16]
#p = [4]
Dcutoff = 0.05
## IMPORTANT
# Dcutoff for p=16 is 0.02 0.02 0.01
# Dcutoff for p=12 is 0.02 0.01 0.05 
# Dcutoff for p=8 is  0.02 0.01 0.008
# Dcutoff for p=4 is  0.04 0.02 0.01
# END

#p = range(4,8,4)
#print p
baseDir = "/home/local/UFAD/rahul.koneru/post_processing/NekExamples/sod3_ALL/steps"
refDir = "/_output"
refFile = "/fort.q0010"
#refParts = (baseDir, refDir, refFile)
#print "".join(refParts)
#rhoFile = "/logfile"
rhoFile = "/step"
syms = ['k','r','b','--k','--r','--b']
syms2 = ['r^','rs','or']
syms3 = ['b^','bs','ob']
ref_x = np.linspace(-5.0, 5.0, num=20000)

count = 0
l = 0
arr_err_l1   = np.zeros((len(N)*len(p)))
arr_err_l2   = np.zeros((len(N)*len(p)))
arr_err_linf = np.zeros((len(N)*len(p)))
#arr_err[0] = 1
#print arr_err[0]
#plt.ion()
#plt.show()
indx = 0
print(' N    p    CFL       Dmu       AV')
print('-------------------------------------')
for indxp, i in enumerate(p):
#    print indxp
    leg = 1
    for indxN, j in enumerate(N):
#        print indxN
#        leg = 1
        currFolderParts = ("/N",str(j),"_p",str(i))
        currFolder = "".join(currFolderParts)
#        print currFolder
        currFileParts = (baseDir,currFolder,rhoFile)
#        fileNP = np.loadtxt("".join(currFileParts))
        currFile = "".join(currFileParts)
#        logFile  = open(currFile,'r')
#        for line in logFile: 
#        print logFile.readline(100)

        with open(currFile,'r') as logFile:
            for line in logFile:
                if line.startswith('CMT'):
                    words = line.split()
#                    print words[3],words[7]
                    nsteps = words[1].replace(',','')
#        print ( 'nsteps=%6i' % int(nsteps) )
        
        data = np.zeros((int(nsteps),5,len(N)*len(p)))
        with open(currFile,'r') as logFile:
            for line in logFile:
                if line.startswith('CMT'):
                    words = line.split()
                    step = words[1].replace(',','')
                    t   = words[3].replace(',','')
                    cfl = words[7].replace(',','')
                    dmu = words[9].replace(',','')
                    knd = words[10].replace(',','')
                    art = words[11].replace(',','')
                    data[int(step)-1,0,indx] = float(t)
                    data[int(step)-1,1,indx] = float(cfl)
                    data[int(step)-1,2,indx] = float(dmu)
                    data[int(step)-1,3,indx] = float(knd)
                    data[int(step)-1,4,indx] = float(art)
                    if abs(float(t)-Dcutoff) <= 1E-10:
                        cutoff = int(step)-1 
#                        print cutoff, float(t)
#                    print ('dt=%s, CFL=%s' % (dt,cfl))
#                    print ( 'dt=%6.4E, CFL=%6.4E, D_mu=%6.4E' % (float(t),float(cfl),float(dmu)) )
#                    with open("out.log",'w') as out:
#                        out.write(dt)
#                        out.write(cfl)
#                    plt.plot(float(t),float(cfl),'or', ms=4)
#                    print words
#        print('N=%s, p=%s, L1=%5.3E, L2=%5.3E, Linf=%5.3E' % (str(j),str(i),l1,l2,linf) )
        l = l+1
#        print j,'','','',i,'','','',cfl
#        print('%3i %3i %5.3E' % (j,i,float(cfl)) )
        avgCFL = np.mean(data[cutoff:,1,indx])
        avgDmu = np.mean(data[cutoff:,2,indx])
        avgAV  = np.mean(data[cutoff:,4,indx])
        with open("out2.log",'a') as out:
#            out.write(dt)
#            out.write(cfl)
            if indx == 0:
                out.write(' N    p    CFL       Dmu       AV\n')
                out.write('-------------------------------------\n')
            out.write('%3i %3i %5.3E %5.3E %5.3E\n' % (j,i,avgCFL,avgDmu,avgAV) )
#        print('%5.3E %5.3E %5.3E' % (avgCFL,avgDmu,avgAV))
#        fig1 = plt.figure(1)
#        ax1 = fig1.add_subplot(2,1,1)
#        ax1.plot(data[:,0,indx],data[:,1,indx],syms[indx], linewidth=2 , label=r'$p = $ %i' % i if leg==1 else "")
##
#        ax2 = fig1.add_subplot(2,1,2)
#        ax2.plot(data[:,0,indx],data[:,2,indx],syms[indx], linewidth=2 , label=r'$p = $ %i' % i if leg==1 else "")
       
#        ax3 = fig1.add_subplot(3,1,3)
#        ax3.plot(data[:,0,indx],data[:,4,indx],syms[indx], linewidth=2 , label=r'$p = $ %i' % i if leg==1 else "")
#        ax1.loglog(1.0/j,l1,syms[count], ms=8, label=r'$p = $ %i' % i if leg==1 else "")
#        fig2 = plt.figure(2)
#        ax2 = fig2.add_subplot(1,1,1)
#        ax2.loglog(1.0/j,l2,syms2[count], ms=8, label=r'$p = $ %i' % i if leg==1 else "")
#        plt.loglog(1.0/j,linf,syms3[count], ms=8, label=r'$p = $ %i' % i if leg==1 else "")
        leg = 0
        indx += 1

    count = count+1

ax1.legend()
ax1.set_xlabel(r'$t(s)$', fontsize=14)
ax1.set_ylabel(r'$CFL$', fontsize=14)
ax1.set_xlim([-0.0,0.05])
#
ax2.legend()
ax2.set_xlabel(r'$t(s)$', fontsize=14)
ax2.set_ylabel(r'$D_\mu$', fontsize=14)
ax2.set_xlim([-0.0,0.05])
#plt.close(fig2)
#
#figTitle = '/sod3_conv.png'
#figParts = (baseDir,figTitle)
##plt.savefig(''.join(figParts))
##plt.savefig(''.join(figParts), bbox_inches='tight')
##plt.savefig('conv_v1.png')
##plt.draw()
##plt.ion()
##plt.pause(5.0)
plt.show()


