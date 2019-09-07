#!/usr/lcoal/env/python2.7

import socket
import re
import os
mjst = '/home/pi/mjpg-streamer/mjpg-streamer-experimental/'

UDP_IP = "10.8.0.6"
UDP_PORT = 1195

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data
    # Reboot system when "reboot" request received
    if re.compile(data).search('reboot'):
                  os.system("notify-send 'Reboot' 'NOW' && mpg123 /home/user/Music/rebooting.mp3 && reboot")
    if re.compile(data).search('playmusic'):
                  os.system("notify-send 'Music' 'Playing' && mpg123 /home/user/Music/playmusic.mp3 && mpg123 -z /home/user/Music/casey-neistat-music28Oct2016/*.mp3 &")
    if re.compile(data).search('stopmusic'):
                  os.system("notify-send 'Music' 'Stop' && mpg123 /home/user/Music/stopmusic.mp3  && killall mpg123")
    if re.compile(data).search('shutdown'):
                  os.system("notify-send 'Shutdown in 10sec' &&  mpg123 /home/user/Music/systemshutdown.mp3  && sleep 5 && mpg123 /home/user/Music/count5.mp3 && poweroff")
    if re.compile(data).search('update'):
                  os.system("notify-send 'Update' 'Started' && mpg123 /home/user/Music/updating.mp3  && gnome-terminal -e 'sudo dnf -y upgrade'")
    if re.compile(data).search('visitors'):
                  os.system("notify-send 'Visitor' 'in backyard' && mpg123 /home/user/Music/visitors.mp3")
    if re.compile(data).search('lockdown'):
                  os.system("notify-send 'Lock Down' 'Now' && mpg123 /home/user/Music/lockdown.mp3 && gnome-screensaver-command -l")
    if re.compile(data).search('foundman'):
                  #os.system("notify-send 'Man' 'Detected' && mpg123 /home/user/Music/Man-Found-JA.mp3")
                  os.system("mpg123 /home/user/Music/beep-07.mp3")
    f = open('/home/user/Workspace/word.txt', 'w')
    f.write(data)
    f.close()

