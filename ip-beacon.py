#!/usr/bin/python3

from socket import *
import time
import sys
import re
import subprocess


while True:
    p = subprocess.run('/sbin/ip addr | /bin/grep "inet "', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    brds = []
    for line in p.stdout.split(b'\n'):
        m = re.search(rb'inet (\d+\.\d+\.\d+\.\d+).* brd (\d+\.\d+\.\d+\.\d+) ', line)
        if m:
            brds.append((m.group(1), m.group(2)))

    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

    for ipaddress, brd in brds:
        s.sendto(b"host=%s" %(gethostname().encode('ascii')), (brd, 37001))
        print("%s\t%s" % (ipaddress.decode('ascii'), brd.decode('ascii')))
    time.sleep(10)
    s.close()
