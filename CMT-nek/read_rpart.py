#!/usr/bin/python
##
# In the rpart* files, each particle has 42 entries each of size 'prec'
# with the very first entry being the total no.of particles.
# DATA LAYOUT
# Particle Position [ x  y  z] = rows 2 3 4 , 5-13 history values
# Particle Velocity [vx vy vz] = rows 14 15 16, 17-25 history values
# Fluid Velocity    [ux uy uz] = rows 26 27 28, 29-37 history values
# Diameter = row 38
# Super-particle loading = row 39
# Temperature = row 40
# Particle id = rows 41 42 43

import matplotlib.pyplot as plt
import numpy as np
import struct

#fid = open('UQ1_rpart00001','rb')

fid = open('rpart00001_old', 'rb')

f = fid.read()  # Binary read
prec = 'f' # Prescision
size = struct.calcsize(prec)
#npcls = struct.unpack(prec, f[0:size])          # No.of pcls
#x = struct.unpack(prec, f[4:8]) # x-coords
#y = struct.unpack(prec, f[8:12]) # y-coords
#z = struct.unpack(prec, f[12:16]) # z-coords

d = list(struct.iter_unpack(prec, f))
npcls = d[0]          # No.of pcls
x = d[1:len(d):42] # x-coords
y = d[2:len(d):42] # y-coords
z = d[3:len(d):42] # z-coords
#xyz = [x y z];

fid.close()
