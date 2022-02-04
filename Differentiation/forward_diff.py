import numpy
import math
import matplotlib.pyplot as plt

def wave(f,g,l,r,a,b,t,c,h,k):

    m=(b-a)/h
    m=int(m)
    n=t/k
    n=int(n)
    T=numpy.linspace(0,t,n+1,endpoint='true')
    sigma=(c*k)/h
    w=numpy.zeros((m+1,n+1))
    for i in range(0,m+1):
        w[i,0]=f(a+(i*h))
    for i in range(0,n+1):
        w[0,i]=l(i*k)
        w[m,i]=r(i*k)
    for i in range(1,m):
        w[i,1]=(1-(sigma**2))*w[i,0]+(k*g(a+(i*h)))+(((sigma**2)/2)*(w[i-1,0]+w[i+1,0]))
    for j in range(2,n+1):
        for i in range(1,m):
            w[i,j]=(2-(2*sigma*sigma))*w[i,j-1]+((sigma*sigma)*w[i-1,j-1])+(sigma*w[i+1,j-1])-(w[i,j-2])
    return T,w

def fn(x):
    return math.sin(math.pi*x)
def G(x):
    return 0
def L(x):
    return 0
def R(x):
    return 0

t,X=wave(fn,G,L,R,0,1,1,2,0.1,0.01)

for i in range(0,11):
    plt.plot(t,X[i,0:])
plt.show()
