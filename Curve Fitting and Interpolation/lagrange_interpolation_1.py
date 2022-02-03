#!/usr/bin/env python3

# Lagrange interpolation
import numpy as np
import scipy.special 
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as tic


datafile = 'bessel_table.txt'
data = np.genfromtxt(datafile,comments='#',usecols=(0,1))

def lagrange_interpolate(xv, yv):
    """
    xv and yv are lists of x and y values
    """
    num_points = len(xv)
    def poly(x):
        pval = 0.0
        for i in range(num_points):
            factor = 1.0
            for j in range(num_points):
                if j!=i:
                    factor = factor * (x - xv[j])/(xv[i] - xv[j])
            pval = pval + yv[i] * factor
        return pval
    return poly

xv = data[:,0]
yv = data[:,1]
lagrange_poly = lagrange_interpolate(xv, yv)
#print(lagrange_poly(1.2))
#print(lagrange_poly(100.0))


t = np.arange(0.0, 10.0, 0.5)
fig = plt.figure()
ax = fig.add_subplot(111)
# The Bessel function
#ax.plot(t, scipy.special.jv(0, t))
ax.plot(data[0:10,0], data[0:10,1], 'ro')

# interpolating poly
ax.plot(t, lagrange_poly(t), '--')

ax.xaxis.set_major_locator(tic.MultipleLocator(1.0))
plt.show()
