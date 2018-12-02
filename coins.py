#!/usr/bin/python                                                                     

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Simulator for diffusion out of urn
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
# Function to simulate game coins
def run_sim(N):
    counter1 = 0
    counter2 = 0

    while counter1 < N and counter2 < N:
        counter1 += random.randint(0, 1)
        counter2 += random.randint(0, 1)

    return counter1 == N

#============================================================================#
# Function to run k simulations of coin game with N coins
# Returns percentage wins
def run_k_sim(N, k):
    return sum(map(run_sim, [N] * k))

###########################################                                                                                                       
###              MAIN SCRIPT            ###                                                                                                        
###########################################                                                                                                        

N = 10
num_trials = 10000

print 'player 1 won %d out of %d' % (run_k_sim(N, num_trials), num_trials)
