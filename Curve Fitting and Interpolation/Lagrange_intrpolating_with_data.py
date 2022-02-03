import numpy
import math
import matplotlib.pyplot as plt

def interp(data):
    m,l=data.shape
    def fn(x):
        n=len(x)
        poly=numpy.zeros(n)
        for i in range(0,n):
            
            
            for j in range (0,m):
                L=1
                for k in range(0,m):
                    if k!=j:
                        L=L*(x[i]-data[k,0])/(data[j,0]-data[k,0])
                poly[i]=poly[i]+(data[j,1]*L)
        return poly
    return fn


Data=numpy.array([(0,100),(5700,50),(11400,27),(17100,12),(22800,7),(28500,2)])
func=interp(Data)
x=numpy.array([10000])
y=func(x)
print("% remaining at 10000 years = ",y)

X=Data[0:,0]
Y=Data[0:,1]
Z=numpy.linspace(0,28500,500,endpoint=True)
plt.plot(X,Y,'yo')
plt.plot(Z,func(Z))
plt.plot([10000],func([10000]),'ro')
plt.show()



            
                
            
        
        
        
        
