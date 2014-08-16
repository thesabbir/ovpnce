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
    ovpn = re.sub('<cert>(.*)<\/cert>|<ca>(.*)<\/ca>|<key>(.*)<\/key>|<tls-auth>(.*)<\/tls-auth>', '', client, flags=re.S)
    ovpn = re.sub('key-direction\s1', 'ca ca.crt\ncert client.crt\nkey client.key\ntls-auth ta.key 1', ovpn)
    files = {
    'ca.crt' : ca,
    'ta.key' : ta,
    'client.crt' : cert,
    'client.key' : key,
    'client.ovpn' : ovpn
    }
    return files


def WriteFiles(files):
    print "Writing configarations..."

    os.makedirs('openvpn_config', mode=0755)
    os.chdir('openvpn_config')
    for file in files:
        print 'Writing "%s"...' % file
        temp_file = open(file, 'w')
        temp_file.write(files[file])
        temp_file.close()


try:
    client = ReadFile(config_file)
    files = Extract(client)
    WriteFiles(files)

except Exception, e:
    print "Error : ", e
