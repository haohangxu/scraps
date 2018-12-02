#!/usr/bin/python

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Name: Haohang Xu
# Date: 10/1/2015
#
# Some experimentation with multithreaded programming
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###########################################
###               IMPORTS               ###
###########################################

import random
import threading

###########################################
###                GLOBALS              ###
###########################################


###########################################
###                 CLASSES             ###
###########################################

#==============================================================================
# Define thread class
class Print_thread (threading.Thread):
  def __init__(self, to_print):
    threading.Thread.__init__(self)
    self.to_print = to_print

  def run(self):
    while True:
      print self.to_print

###########################################
###            FUNCTION DEFS            ###
###########################################

#==============================================================================
# Define function to start three threads that print 1, 2, and 3
def start_threads ():
  thread1 = Print_thread(1)
  thread2 = Print_thread(2)
  thread3 = Print_thread(3)

  thread1.start()
  thread2.start()
  thread3.start()

###########################################
###            MAIN FUNCTION            ###
###########################################

start_threads()