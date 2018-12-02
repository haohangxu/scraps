#!/usr/bin/env python

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Script for finding generators of Z/nZ for large n.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


###########################################
###          FUNCTION DEFS              ###
###########################################

#============================================================================#
# Finds the order of element a in Z/nZ
def find_order(a, n):
	return lcm(a, n)/a

#============================================================================#
# Finds the generators of Z/nZ
def find_generators(n):
	result = []
	for i in range(1, n):
		if find_order(i, n) == n:
			result.append(i)

	return result

#============================================================================#
# Prints the given generators in LaTeX
def print_latex(generators):
	map()
	for g in generators:
		result = result + "$" + str(g) + "$"