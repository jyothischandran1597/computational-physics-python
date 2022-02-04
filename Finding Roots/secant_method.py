#!/usr/bin/env python3
"""
Secant method
"""
import sys
import math

def is_equal(a, b):
	"""
	Check if floats `a' and `b' are equal within the machine precision
	"""
	return abs(a-b) < sys.float_info.epsilon

def secant(f, a, b, TOL=1.0E-8, max_iter=100):
	"""
	f is the cost function, f_prime is first derivative, 
	a is the initital guess. TOL is tolerance.
	`max_iter' is the maximum number of iterartion.
	"""
	x = a
	x_1=b
	f_x = f(x)
	f_x_1=f(x_1)
	iter = 0
	while (iter < max_iter):
		step_size = -f_x*(x-x_1)/(f_x-f_x_1)
		x = x + step_size
		f_x = f(x)
		if is_equal(f_x, 0.0) or abs(step_size)<TOL:
		#if math.isclose(f_x, 0.0, abs_tol=1.0E-6):
			return (x, iter) 
		iter = iter + 1
	return False

def func(x):
	"""
	f(x) = cos(x) - x	
	"""
	return math.cos(x) - x


# the root
root, iter = secant(func, 1, 0.6)

print("Iterartion = ", iter)
print("root = ", root, ",func = ", func(root))




















