#!/usr/bin/python

# Rename SDyzavg file to SD_###.dat file

import sys
import glob, os

# Load the current contents of the dir
sd2dparts = (os.getcwd(),'/2D_SD')
sd2dparts = (os.getcwd())
dirsd2d = "".join(sd2dparts)
files2d = os.listdir(dirsd2d)
files2d = glob.glob('2D_SD/*yz*')

# Need to add an exception to check if there are any *SDyz* files
for i in files2d:
#	temp = i.split('_')
#	temp = i.split('.SDavg_')
	temp = i.split('.yzavg_')

	temp = temp[1].replace('.dat','')
	temp = float(temp)*1e+6
	t = int(temp)
	t = "%03d" % temp
	print i,t

	currfileparts = (dirsd2d,"/",i)
	currfileparts = (dirsd2d,"/",i)
	currfile = "".join(currfileparts)
#	renfileparts = (dirsd2d,"/","SD_",t,".dat")
	renfileparts = (dirsd2d,"/2D_SD/","YZ_",t,".dat")
	renfile = "".join(renfileparts)
#	print currfile
#	print renfile

	os.rename(currfile,renfile)

renfiles2d = sorted(os.listdir(dirsd2d))

