#!/usr/bin/python

#import matplotlib.pyplot as plt
import numpy as np
#import sys
import os,glob
import h5py as h5
#from itertools import islice

# Initial conditions
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

home = os.getcwd()
home  = 'M166/NoGap'
src = '/21/1'
avgfiles = home+src+'/*.yzav*'
hfile = home+src+'/yzavg.hdf5'
mes10 = glob.glob(avgfiles)
#mes10 = glob.glob('Mesoscale/NoFluc/M3pt0/tests/phi10_no_qs_intrp1/*SOL*/*forces*')
#mes10_dp5 = sorted(mes10, key=lambda time: float(time[-11:]))

files = sorted(mes10, key=lambda time: float(time[-15:-4]))

def writeh5file(grp_name):
    hf = h5.File(hfile,'a')
    grp = hf.create_group(grp_name)
    grp.attrs['time'] = t
    grp.create_dataset('x', data=x)
    grp.create_dataset('rhog', data=rhog)
    grp.create_dataset('pg', data=pg)
    grp.create_dataset('Tg', data=tg)
    grp.create_dataset('ugmag', data=ugmag)
    grp.create_dataset('ug', data=ug)
    grp.create_dataset('vg', data=vg)
    grp.create_dataset('wg', data=wg)
    if col == 9:
        grp.create_dataset('phip', data=phip)
    hf.close()

def set_attrs():
    hf = h5.File(hfile,'a')
    hf.attrs['Mach'] = 1.66
    hf.attrs['dp'] = 115E-6
    hf.attrs['curtain_width'] = 2E-3
    hf.attrs['phi'] = 0.21
    hf.attrs['Curtain'] = 'Top-hat'
    hf.attrs['Gap'] = 'No'
    hf.close()

for indx, i in enumerate(files[:]):

    print (i)
    t = i.split('_')[-1].split('.dat')[0]
    t = float(t)
    f = np.loadtxt(i)
    row, col = f.shape
    x = f[:,0]
    rhog = f[:,1]
    pg = f[:,2]
    tg = f[:,3]
    ugmag = f[:,4]
    ug = f[:,5]
    vg = f[:,6]
    wg = f[:,7]
    if col == 9:
        phip = f[:,8]

    t = t*1E+6
    writeh5file('time'+'%03d' % t)

set_attrs()
