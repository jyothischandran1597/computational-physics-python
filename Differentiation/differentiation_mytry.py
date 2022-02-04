# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 17:51:26 2019

@author: hp
"""
import numpy as np

def f(x):
    func=1.0/x
    return func

def f_d1(x):
    func_d1=-1.0/(x*x)
    return func_d1

def f_d2(x):
    func_d2=2.0/(x*x*x)
    return func_d2

def f_d3(x):
    func_d3=-6.0/(x*x*x*x)
    return func_d3

def derivative_forward_diff(x,h):
    derivative1=(f(x+h)-f(x))/h
    error_min1=h*0.5*f_d2(x)
    error_max1=h*0.5*f_d2(x+h)
    exact_error1=derivative1-f_d1(x)
    return derivative1,[error_min1,error_max1], exact_error1

def derivative_centered_diff(x,h):
    derivative2=(f(x+h)-f(x-h))/(2*h)
    error_min2=h*h*(1.0/6)*f_d3(x-h)
    error_max2=h*h*(1.0/6)*f_d3(x+h)
    exact_error2=derivative2-f_d1(x)
    return (derivative2,[error_min2,error_max2],exact_error2)

d1,e_range,e_exact=derivative_forward_diff(2.0,0.1)
print("Forward difference: f'(2)= ", d1," with error between ",e_range[0]," and ",e_range[1]," with exact error",e_exact)

d2,e_range,e_exact=derivative_centered_diff(2.0,0.1)
print("Centered difference: f'(2)= ", d2," with error between ",e_range[0]," and ",e_range[1]," with exact error",e_exact)
