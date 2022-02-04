#! /usr/bin/env/python3

import sys
import math

def equal(a,b):

	return abs(a-b) < sys.float_info.epsilon  	# Checks whether a and b are within machine precision
	
	
def regula_falsi(f,a,b,TOL=1.0E-15,MAX_ITR=100):# Function to execute Regula Falsi method			

	iter = 0
	while iter<MAX_ITR :							
	
		step = -f(a)*(a-b)/(f(a)-f(b))		
		c = a + step 							# X-Intercept of the secant between the bracket ends
		
		if equal(f(c),0.0) or abs(b-a)<TOL :
			return (c,iter)
			
		elif  f(a)*f(c)<0.0 :					# Usual Bisection procedure									
			b = c
			
		else :
			a = c
		iter = iter + 1
		
	return None
		
def fun(x):										# The cost function						

	return math.exp(x) + math.sin(x) - 4
	
print("\n\n\tREGULA FALSI METHOD TO FIND ROOT\n\n")

print("f(x) = e^x + sin x -4")

root, iter = regula_falsi(fun,0,1)

print ("\nRoot of the function is ", root)	
print("\nThe answer was found in ", iter, " iterations") 
