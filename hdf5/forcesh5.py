#!/usr/bin/python

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

# File Name : forcesh5.py

# Purpose : Open force files and copy 
#           data to a hdf5 file.
#           File attributes have to be 
#           set manually.

# Creation Date : 05-15-2018

# Last Modified :

# Created By : Rahul Koneru 

#_._._._._._._._._._._._._._._._._._._._._.

import numpy as np
import os,glob
import h5py as h5
#from itertools import islice

mes10 = glob.glob('Mesoscale/NoFluc/tests/dp5mic/*forces*')
files = sorted(mes10, key=lambda time: float(time[-11:]))

def readTime():
#    print(line)  # Uncomment for debugging
    varOut = float(next(ffile))
    varOut = varOut #*1e6
    return varOut

def readDim():
#    print(line)  # Uncomment for debugging
    varOut = int((next(ffile).split())[0])
    return varOut

def readData():
#    print(line)  # Uncomment for debugging
    varOut = np.zeros((arrDim)) 
    for k in range(0,int(arrDim/5)):
        tmp = ((next(ffile).split(',')))
        for j in range(0,5):
            varOut[j+5*k] = float(tmp[j])
    return varOut

def readData2():
    print(line)
    varOut = np.zeros((arrDim)) 
    for k in islice(ffile,int(arrDim/5)):
        print(k)
    print(k)
    return k

def writeh5file(grp_name):
    hf = h5.File('forces2.hdf5','a')
    grp = hf.create_group(grp_name)
    grp.attrs['time'] = t
    grp.create_dataset('xyz', data=np.transpose([x,y,z]))
    grp.create_dataset('Fqs', data=np.transpose([qsx,qsy,qsz]))
    grp.create_dataset('Fpg', data=np.transpose([pgx,pgy,pgz]))
    grp.create_dataset('Fiu', data=np.transpose([iux,iuy,iuz]))
    grp.create_dataset('Fvu', data=np.transpose([vux,vuy,vuz]))
    grp.create_dataset('Ftot', data=np.transpose([fx,fy,fz]))
    hf.close()

# Need to set 'dp' and 'dx' manually
def set_attrs():
    hf = h5.File('forces2.hdf5','a')
    hf.attrs['npcls'] = arrDim
    hf.attrs['dp'] = 5E-6
    hf.attrs['dx'] = 10E-6
    hf.close()

k = 0
for indx, i in enumerate(files[:]):

    print (i)
    with open(i,'r') as ffile:
        for count, line in enumerate(ffile):
            if line.startswith('# Physical time'):
                t = readTime()
                print(t)
            if line.startswith('# Dimensions'):
                arrDim = readDim()
                print(arrDim)
            if line.startswith('# Pcl x-coordinate'):
                x = readData()
            if line.startswith('# Pcl y-coordinate'):
                y = readData()
            if line.startswith('# Pcl z-coordinate'):
                z = readData()
            if line.startswith('# QS force x'):
                qsx = readData()
            if line.startswith('# QS force y'):
                qsy = readData()
            if line.startswith('# QS force z'):
                qsz = readData()
            if line.startswith('# PG force x'):
                pgx = readData()
            if line.startswith('# PG force y'):
                pgy = readData()
            if line.startswith('# PG force z'):
                pgz = readData()
            if line.startswith('# IU force x'):
                iux = readData()
            if line.startswith('# IU force y'):
                iuy = readData()
            if line.startswith('# IU force z'):
                iuz = readData()
            if line.startswith('# VU force x'):
                vux = readData()
            if line.startswith('# VU force y'):
                vuy = readData()
            if line.startswith('# VU force z'):
                vuz = readData()
            if line.startswith('# Total force x'):
                fx = readData()
            if line.startswith('# Total force y'):
                fy = readData()
            if line.startswith('# Total force z'):
                fz = readData()
	

    writeh5file('time'+str(indx))

set_attrs()
