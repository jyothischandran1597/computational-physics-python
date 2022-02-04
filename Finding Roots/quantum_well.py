#!/usr/bin/env python3

"""
Program to find ground state energy of a particle in a 1D finite square well potential.
"""

import sys
import math
import collections

def bisection(f, quantum_well, a, b, TOL=0.001, MAX_ITER=100):
	"""
	f is the cost function, [a,b] is the initial bracket, TOL is tolerance, MAX_ITER is maximum iteration 
	"""

	f_a = f(a, quantum_well)
	f_b = f(b, quantum_well)

	iter = 0
	while iter < MAX_ITER:
		c = (a+b)/2
		f_c = f(c, quantum_well)

		if math.isclose(f_c, 0.0, abs_tol=1.0E-6) or abs(b-a)/2<TOL:
			return (c, iter)
		else:
			if f_a * f_c < 0:
				b = c
				f_b = f_c
			else:
				a = c
				f_a = f_c

			iter = iter + 1
	return False

def func(E, system):
	"""
	The cost function: f(E) = beta * cos(alpha*a) - alpha * sin(alpha * a)
	Mass is in units of m_e  
	Energy is in units of eV 
	Distance is in Angstroms
	"""
	alpha = math.sqrt(2 * system.mass * E / system.h_bar_sq ) 
	beta = math.sqrt(2 * system.mass * (system.V0 - E) / system.h_bar_sq ) 
	f = beta * math.cos(alpha * system.a) - alpha * math.sin(alpha * system.a)
	return f

system = collections.namedtuple('system', ['h_bar_sq', 'a', 'V0', 'mass'])

quantum_well = system(h_bar_sq=7.6199682, a=3.0, V0=10.0, mass=1)

a = 0
b = 1
root, iter = bisection(func, quantum_well, a, b, TOL=1.0E-12)

print("Iteration = ", iter)
print("Energy = ", root, "eV, func = ", func(root, quantum_well))

