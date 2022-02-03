#!/usr/bin/env python3

import numpy as np
datafile = './velocity_time.txt'
data = np.genfromtxt(datafile,comments='#',usecols=(0,1))

def linear_fit(xdata, ydata):
    m = len(xdata)
    n = 2
    # Construct the A matrix
    A = np.zeros((m,2))
    for i in range(m):
        A[i,0] = 1
        A[i,1]=xdata[i]
    #print(A)
    M = np.dot(np.transpose(A),A)
    b = np.dot(np.transpose(A),ydata)
    p = np.linalg.solve(M, b)
    return p

params = linear_fit(data[:,0], data[:,1])
print(params)

# Verify
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as tic

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(data[:,0], data[:,1],'ro')
xmin = data[0,0]
xmax = data[-1,0]
xp = np.linspace(xmin, xmax, 10)
c1 = params[0]
c2 = params[1]
ax.plot(xp, c1+c2*xp, 'b-')
plt.show()