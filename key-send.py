#!/usr/local/bin/python
import socket
while True:
  key = input("Press 1:Run mjpgst, 2:Switch CAM, 4:Kill  |   9:Run motion, 0:Kill ")
#while key != "": 
  if key == 1:
    a = "getstream"
  elif key == 2:
    a = "restream"
  elif key == 4:
    a = "stopstream"
  elif key == 9:
    a = "startmotion"
  elif key == 0:
    a = "stopmotion"
  UDP_IP = "IP address"
  UDP_PORT = PortNumber 
  MESSAGE = (a)
  print "UDP target IP:", UDP_IP
  print "UDP target port:", UDP_PORT
  print "message:", MESSAGE

  sock = socket.socket(socket.AF_INET, # Internet
                 socket.SOCK_DGRAM) # UDP
  sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
