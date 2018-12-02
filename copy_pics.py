#!/usr/bin/env python

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Name: Haohang Xu
# File: copy_pics.py
#
# Copies the pictures given in a text file from a directory into a new directory.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###########################################
###               IMPORTS               ###
###########################################

import os
import copyfile

###########################################
###           FUNCTION DEFS             ###
###########################################

def copy_file(src, name, dest):
	if name in os.listdir(src):
		copyfile()