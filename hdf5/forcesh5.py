#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import sys
import os,glob
import h5py as h5
from itertools import islice

Ms = 3.0 ;
p = 101325 ;
rho = 1.2048 ;
gamma = 1.4 ;
R = 287.0
us = Ms*np.sqrt(gamma*p/rho) ;
dp = 100E-6 ;
tau = dp/us ;
x_shock = 0.12
x_curt = 0.15
curt_width = 3.5e-3
phi = 0.10
rho2 = 4.64670
p2 = 1047025.0
u2 = 7.625535638079468E+02

phis = [10.0,15.0,20.0,25.0]

mes10 = glob.glob('Mesoscale/NoFluc/tests/dp5mic/*forces*')
#mes10_dp5 = sorted(mes10, key=lambda time: float(time[-11:]))

#files = [mes10_dp5]
files = sorted(mes10, key=lambda time: float(time[-11:]))

def readTime():
    print(line)
    varOut = float(next(ffile))
    varOut = varOut #*1e6
    return varOut

def readDim():
    print(line)
    varOut = int((next(ffile).split())[0])
    return varOut

def readData():
    print(line)
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

def set_attrs():
    hf = h5.File('forces2.hdf5','a')
    hf.attrs['npcls'] = arrDim
    hf.attrs['dp'] = 5E-6
    hf.attrs['dx'] = 10E-6
    hf.close()

cst = 1
k = 0
for indx, i in enumerate(files[:]):

    print (i)
#    with open(i[indx],'r') as ffile:
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
