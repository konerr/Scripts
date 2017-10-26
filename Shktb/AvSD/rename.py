#!/usr/bin/python

# Rename SDyzavg file to SD_###.dat file

import sys
import os

# Load the current contents of the dir
sd2dparts = (os.getcwd(),'/2D_SD')
dirsd2d = "".join(sd2dparts)
files2d = os.listdir(dirsd2d)

# Need to add an exception to check if there are any *SDyz* files
for i in files2d:
	temp = i.split('_')
	temp = temp[1].replace('.dat','')
	temp = float(temp)*1e+6
	t = int(temp)
	t = "%03d" % temp

	currfileparts = (dirsd2d,"/",i)
	currfile = "".join(currfileparts)
	renfileparts = (dirsd2d,"/","SD_",t,".dat")
	renfile = "".join(renfileparts)

	os.rename(currfile,renfile)

renfiles2d = sorted(os.listdir(dirsd2d))

