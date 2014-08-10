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
    ca = re.search('<ca>(.*)<\/ca>', client, flags=re.S ).group(1)
    cert = re.search('<cert>(.*)<\/cert>', client, flags=re.S ).group(1)
    key = re.search('<key>(.*)<\/key>', client, flags=re.S ).group(1)
    ta = re.search('<tls-auth>(.*)<\/tls-auth>', client, flags=re.S ).group(1)
    files = [ca, cert, key, ta]
    return files
    

def WriteFiles(files):
    print "Writing configarations..."
    for file in files:
        print file, '\n'
    return files

try:
    client = ReadFile(config_file)
    files = Extract(client)
    WriteFiles(files)

except Exception, e:
    print "Error : ", e


