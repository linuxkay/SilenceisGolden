# Windows version of silicenisgolden.py Built by linuxkay@
#!/usr/lcoal/env/python2.7
# netstat -nao to check socket status

import socket
import re
# for lock screen.
import ctypes

UDP_IP = "IP"
UDP_PORT = port_number

sock = socket.socket(socket.AF_INET, # Internet
                    #socket.SOCK_DGRAM) # UDP
                     socket.SOCK_STREAM) # TCP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received message:", data)
    # Lock Screen when "lockdown" request received
    if re.compile(data.decode("utf-8")).search('lockdown'):
                 ctypes.windll.user32.LockWorkStation()
    f = open(r'C:\Users\User_Name\program_spaces\word.txt', 'w')
    f.write(data.decode("utf-8"))
    f.close()
