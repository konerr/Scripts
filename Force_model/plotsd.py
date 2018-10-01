#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import sys
import os

plt.rc('text', usetex=True)
plt.rc('font', weight='bold')
plt.rc('axes', linewidth=1.4)
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

rho = 2.475479287947678
u = 4.024042252941134e+02
p = 3.418928266666666e+05
T = 481.22568
x_shock = 0.12
x_curt = 0.15
curt_width = 3.5e-3
dp = 115e-6
phi = 0.18

lines = ['r','b','g','c']
syms = ['--r','--b','--g','--c']
syms1 = ['o-r','o-b','o-g','o-c']
syms2 = ['x-r','x-b','x-g','x-c']

sd2dparts = (os.getcwd(),'/2D_SD')
dirsd2d = "".join(sd2dparts)
files2d = sorted(os.listdir(dirsd2d))

max_rho = np.zeros((2))
max_p = np.zeros((2))
max_u = np.zeros((2))
max_phi = np.zeros((2))
t_rho = 0.0
t_p = 0.0
t_u = 0.0
t_phi = 0.0
#for indx, i in enumerate(files2d[6:12:2]):
for indx, i in enumerate(files2d[0:27]):
	temp = i.split('SD_')
	temp = temp[1].replace('.dat','')
	t = int(temp)

#	print (t,str(t))
#	print ("%03d" % t)
	currfileparts = (dirsd2d,"/",i)
	currfile = "".join(currfileparts)
#	print (currfile)

	f = np.loadtxt(currfile)

        max_rho[1] = max(f[:,1]/rho)
        max_p[1]   = max(f[:,2]/p)
        max_u[1]   = max(f[:,5]/u)
        max_phi[1] = max(f[:,8]/phi)
        if max_rho[1] > max_rho[0]:
           max_rho[0] = max_rho[1]
           t_rho = t
#           print 'Max rho fluc:%4.3E, at time=%d' % (max_rho[0], t)

        if max_p[1] > max_p[0]:
           max_p[0] = max_p[1]
           t_p = t
#           print 'Max p fluc:%4.3E, at time=%d' % (max_p[0], t)

        if max_u[1] > max_u[0]:
           max_u[0] = max_u[1]
           t_u = t
#           print 'Max u fluc:%4.3E, at time=%d' % (max_u[0], t)

        if max_phi[1] > max_phi[0]:
           max_phi[0] = max_phi[1]
           t_phi = t
#           print 'Max phi fluc:%4.3E, at time=%d' % (max_phi[0], t)

#        plt.figure(1)
#	plt.plot(f[:,0],f[:,1]/rho, lines[indx],label='t=%d' % t )
##        plt.figure(2)
#	plt.plot(f[:,0],f[:,5]/u, syms[indx])
#	plt.plot(f[:,0],f[:,2]/p, syms1[indx])
        plt.figure(1)
	plt.plot(f[:,0],f[:,5]/u,label='t=%d' % t )
        plt.figure(2)
	plt.plot(f[:,0],f[:,2]/p,label='t=%d' % t )
#	plt.plot(f[:,0],f[:,3]/T, syms2[indx])
#	plt.plot(f[:,0],f[:,8]/phi, syms2[indx])

print 'rho fluc:%4.3E, at time=%d' % (max_rho[0], t_rho)
print 'p fluc:%4.3E, at time=%d' % (max_p[0], t_p)
print 'u fluc:%4.3E, at time=%d' % (max_u[0], t_u)
print 'phi fluc:%4.3E, at time=%d' % (max_phi[0], t_phi)
#plt.xlim([0.15,0.165])
plt.legend()
plt.show()


