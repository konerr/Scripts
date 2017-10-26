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
x_shock = 0.12
x_curt = 0.15
curt_width = 3.5e-3
dp = 115e-6
phi = 0.18

sd2dparts = (os.getcwd(),'/2D_SD')
dirsd2d = "".join(sd2dparts)
files2d = sorted(os.listdir(dirsd2d))

#for i in files2d[0:len(files2d):4]:
for i in files2d[0:10:2]:
	temp = i.split('_')
	temp = temp[1].replace('.dat','')
	t = int(temp)

#	print (t,str(t))
#	print ("%03d" % t)
	currfileparts = (dirsd2d,"/",i)
	currfile = "".join(currfileparts)
	print (currfile)

	f = np.loadtxt(currfile)
	plt.plot(f[:,0],f[:,1]/rho, label='t=%d' % t )

plt.xlim([0.12,0.26])
plt.legend()
plt.show()


