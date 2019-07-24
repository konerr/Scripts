#!/usr/bin/python
##
# In the rpart* files, each particle has 42 entries each of size 'prec'
# with the very first entry being the total no.of particles.
# DATA LAYOUT
# Number of particles = 0th entry
# Particle Position [ x  y  z] = rows 1 2 3 , 4-12 history values
# Particle Velocity [vx vy vz] = rows 13 14 15, 16-24 history values
# Fluid Velocity    [ux uy uz] = rows 25 26 27, 28-36 history values
# Diameter = row 37
# Super-particle loading = row 38
# Temperature = row 39
# Particle id = rows 40 41 42

#import matplotlib.pyplot as plt
import numpy as np
import struct

#fid = open('UQ1_rpart00001','rb')

fid = open('rpart00001_old', 'rb')

f = fid.read()  # Binary read
prec = 'f' # Prescision
size = struct.calcsize(prec)
npcls = struct.unpack(prec, f[0:size])          # No.of pcls
#x = struct.unpack(prec, f[4:8]) # x-coords
#y = struct.unpack(prec, f[8:12]) # y-coords
#z = struct.unpack(prec, f[12:16]) # z-coords

for i in range(2):
    dd = list(struct.unpack(42*prec,f[i*42*size+size:(i+1)*42*size+size]))
    print(dd)
d = list(struct.iter_unpack(prec, f))
npcls = d[0]          # No.of pcls
x = d[1:len(d):42] # x-coords
y = d[2:len(d):42] # y-coords
z = d[3:len(d):42] # z-coords
#xyz = [x y z];

fid.close()
