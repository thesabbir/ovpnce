#!/usr/bin/env python

from sys import argv
import os, re

config_file = argv[1]

def ReadFile(file_name):
    print 'Looking for OpenVPN config file "%s" ....' % config_file
    try:
        file = open(config_file, 'r')
        text = file.read()
        file.close()
        return text
    except IOError:
        raise Exception('Unable to open configaration file')
       

def Extract(client):
    print "Extracting config file..."

    

def WriteFiles(**files):
    print "Writing configarations..."


try:
    client = ReadFile(config_file)
except Exception, e:
    print "Error : ", e

