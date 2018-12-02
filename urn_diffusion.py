#!/usr/bin/python                                                                     

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Simulator for diffusion out of urn
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###########################################
###               IMPORTS               ###
###########################################

from math import log

import numpy
import random

###########################################
###            FUNCTION DEFS            ###
###########################################

#============================================================================#
# Function to simulate diffusion out of urn with N balls
def run_sim(N):
    counter = 0
    red_balls = N
    while red_balls > 0:
        counter += 1
        if random.randint(1, N) <= red_balls:
            red_balls -= 1

    return counter

#============================================================================#
# Function to run k simulations of diffusion out of urn with N balls
# Returns list with results
def run_k_sim(N, k):
    return map(run_sim, [N] * k)

#============================================================================#                                                                     
# Function to run k simulations of diffusion out of urn with N balls
# Returns average 
def run_k_sim_avg(N, k):
    return numpy.mean(run_k_sim(N, k))

#============================================================================#                                                                     
# Function to generate hypothesis number for N balls
def get_hypothesis(N):
    return N * (sum(map(lambda x: 1.0/float(x), range(1, N + 1))))

###########################################                                                                                                       
###              MAIN SCRIPT            ###                                                                                                        
###########################################                                                                                                        

trials = range(2, 50)
num_trials = 1000

results = map(lambda N: run_k_sim_avg(N, num_trials), trials)
hypotheses = map(get_hypothesis, trials)

sse = 0

for (a, b) in zip(results, hypotheses):
    print 'result: %f, hypothesis1: %f' % (a, b)
    sse += (a - b) ** 2

print 'sum squared error 1: %f' % sse
