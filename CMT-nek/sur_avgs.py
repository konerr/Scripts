#!/usr/bin/python

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

# File Name : sur_avgs.py

# Purpose : Plot contours of avg values 
# computed from readstep.py 

# Creation Date : 13-10-2017

# Last Modified :

# Created By : Rahul Koneru 

#_._._._._._._._._._._._._._._._._._._._._.

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

f = np.loadtxt('out.log',skiprows=2)

fig1 = plt.figure()
ax = fig1.add_subplot(111, projection='3d')

ax.scatter(f[:,0],f[:,1],f[:,2])
ax.set_xlabel('$N$', fontsize=14)
ax.set_ylabel('$p$', fontsize=14)
ax.set_zlabel('$CFL$', fontsize=14)
ax.set_xticks([50,100,200])
ax.set_yticks([4,8,12,16])
#ax.plot_surface(f[:,0],f[:,1],f[:,2],cmap=cm.coolwarm)
#ax.contour(f[:,0],f[:,1],f[:,2],cmap=cm.coolwarm)
#ax.plot_wireframe(f[:,0],f[:,1],f[:,2])

fig2 = plt.figure()
ax = fig2.add_subplot(111, projection='3d')

ax.scatter(f[:,0],f[:,1],f[:,3])
ax.set_xlabel('$N$', fontsize=14)
ax.set_ylabel('$p$', fontsize=14)
ax.set_zlabel('$D_\mu$', fontsize=14)
ax.set_xticks([50,100,200])
ax.set_yticks([4,8,12,16])
plt.show()
