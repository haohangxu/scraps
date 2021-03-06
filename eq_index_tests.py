#!/usr/bin/python                                                                     

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test generator for google sample code test
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###########################################
###               IMPORTS               ###
###########################################

import numpy
import random

###########################################
###            FUNCTION DEFS            ###
###########################################

#============================================================================#
# Function to generate a sequence of random numbers of length k
def gen(k):
    return map(lambda _: random.randint(-10, 10), [0] * k)

###########################################                                                                                                       
###              MAIN SCRIPT            ###                                                                                                        
###########################################                                                                                                        

for i in range(50):
    print gen(i)
