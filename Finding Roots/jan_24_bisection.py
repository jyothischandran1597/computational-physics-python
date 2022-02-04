#!usr/bin/env python3
import sys
import math as m


def bisection(f,a,b,tol=0.001,max_itr=100):
    f_a=f(a)
    f_b=f(b)
    iter=0
    while iter<max_itr:
        
        c=(a+b)/2
        f_c=f(c)
        if m.isclose(f_c,0.0,abs_tol=1.0E-16) or abs(b-a)/2<tol:
            return (c,iter)
        else:
            if f_a*f_c < 0:
                b=c
                f_b=f_c
            else:
                a=c
                f_a=f_c
            iter = iter+1
    return None


def func(x):
    return x**3-2*(x**2)+(4/3)*x-8/27

root, iter=bisection(func,0,1,tol=1.0E-16)


print("Iteration= ",iter," root= ", root,"  func(x)=", func(root)) 
