# Windows version of silicenisgolden.py Built by linuxkay@
#!/usr/lcoal/env/python2.7

import socket
import re
# for lock screen.
import ctypes

UDP_IP = "192.168.1.22"
UDP_PORT = port-number

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received message:", data)
    # Lock Screen when "lockdown" request received
    if re.compile(data).search(b'lockdown'):
                  ctypes.windll.user32.LockWorkStation()
