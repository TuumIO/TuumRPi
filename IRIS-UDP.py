#!/usr/bin/python

import socket
import sys
import time

UDP_IP = "192.168.1.157"
UDP_PORT = 2390
msg = "VAULT"
 
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("",8888))
except:
    sys.exit()

while(1):
  msgbts = bytes(msg, 'utf-8') #Error de Codificacion????
  s.sendto(msgbts, (UDP_IP, UDP_PORT))
  d = s.recvfrom(1024) #Prender Led cuando se recibe algo?
  time.sleep(300)
