# Silence is Golden 
## Overview 
Using this allows you to control linux over iPhone or Android.

I do not provide how to setup your custome UDP message in your iPhone or Android.
Googling how to send UDP message ios and android will help this easily.

Exmaple:

 Saying Ok google, Shutdown 

then it turns off your system.  

## Demo
No demo

## Description

Sends UDP message over vpn.

You think UDP is unreliable? You are very educated. But have you ever tested how unreliable UDP is by YOURSELF?

UDP is lightning fast.


files

silenceisgolden.py

- It will listen your UDP message and launch commands depending on UDP message. 


## Requirements
vpn connection

python2.7

mpg123

## Usage
Testing

Run py file in terminal.

$ python2.7 silenceisgolden.py

then send udp message from your iPhone or Android.

Set that as customized voice commands

Setting crontab to initiate on boot or add silenceisgolden.py as systemctl services.

for cron

@reboot python2.7 silenceisgolden.py

for systemd

add silenceisgolden.service in /lib/systemd/system/

systemctl-daemon reload

systemctl enable silenceisgolden.service

## Install


## Contribution

## Updates

2022/2/5 Added Windows version.

2020/6/6 key-send.py added for backup.

2017/5/7 created key-send.py

## Licence
[MIT]

## Author

[linuxkay](https://github.com/linuxkay)
