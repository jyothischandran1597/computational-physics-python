#!/usr/bin/env python3

import math

def derivative1(f,x0,h):
    return (f(x0+h)-f(x0))/h

def derivative2(f,x0,h):
    return (f(x0+h)-f(x0-h))/(2.0*h)

def f(x):
    return math.exp(x)

x0 = 0.0
fp_exact = 1.0;

for p in range(1,10):
    h = math.pow(10.0,-p)
    fp1 = derivative1(f, x0, h)
    fp2 = derivative2(f, x0, h)
    err1 = fp_exact - fp1
    err2 = fp_exact - fp2
    print('{:>16.14f} {:>+16.14f}, {:<16.14f}, {:<+16.14f}'.format(fp1,err1,fp2,err2))