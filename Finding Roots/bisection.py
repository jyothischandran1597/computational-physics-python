
import math
from math import sin as sin
from math import log as log


def root(a,b,f):

    i=1
    while i<50:

        c=(a+b)/2
        F_c=f(c)
        F_a=f(a)
        if math.isclose(F_c,0.0,abs_tol=1.0E-8) or abs(b-a)/2<1.0E-10:
            return(c,i)
        else:
            if F_a*F_c<0:
                b=c
            else:
                a=c
            i=i+1

def func1(x):
        return x**5+x-1
def func2(x):
        return sin(x)-(6*x)-5
def func3(x):
        return log(x)+ x*x-3
    

        
proot,p=root(0,1,func1)
print("for fn1 No. of iterations= ",p)
print("root of fn1 = ",proot ," function value at root = ",func1(proot))

sroot,s=root(-1,-2/3,func2)
print("for  fn2  No. of iterations= ",s)
print("root of  fn2 = ",sroot ," function value at root = ",func2(sroot))

lroot,l=root(1,2,func3)
print("for  fn3 No. of iterations= ",l)
print("root of fn3 = ",lroot ," function value at root = ",func3(lroot))
                
                
            
            
            
