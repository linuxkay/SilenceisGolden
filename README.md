# Silence is Golden 
## Overview 
Using this allows you to control linux over iPhone or Android.

Exmaple:

 Saying Ok google, Shutdown 

then it turns off your system.  

# Demo
No demo

## Description

Sends UDP message over vpn.

You think UDP is unreliable? You are very educated. But have you ever tested how unreliable UDP is by YOURSELF?

UDP is lightning fast.


files

silenceisgolden.py

- Establish ssh proxy connection to Raspberry1B+ 


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

## Licence
[MIT]

## Author

[linuxkay](https://github.com/linuxkay)
