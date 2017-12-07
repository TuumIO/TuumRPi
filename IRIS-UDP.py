#!/usr/bin/python

import socket
import getopt
import sys
import time

def usage():
       
       print("Ayuda: IRIS UDP")
       print("")
       print("-d Direccion")
       print("-p Puerto")
       print("-m Mensaje")
       print("-h Ayuda")

def main():
       'Main function'
       global Action, x, y, z, UDP_IP, UDP_PORT, msgbts, s

       try:
              opts, args = getopt.getopt(sys.argv[1:], "d:p:m:h")

       except getopt.GetoptError as err:
              print("Error: "+str(err)+", -h para ayuda\n\n")
              usage()
              sys.exit(2)

       if len(opts) == 0:
              print("Definir atgumentos,  -h for ayuda")
              sys.exit()
       for o, a in opts:
                if o in ("-h"):
                        usage()
                        sys.exit()
                if o in ("-d"):
                        try:
                                UDP_IP = str(a).encode("utf-8")
                        except ValueError:
                                print("-- Direccion")
                                sys.exit(2)
                if o in ("-p"):
                        try:
                                UDP_PORT=int(a)
                        except ValueError:
                                print ("--to argument is taking only numeric values")
                                sys.exit(2)
                if o in ("-d"):
                        try:
                                msgbts = str(a).encode("utf-8")
                        except ValueError:
                                print("-- mensaje")
                                sys.exit(2)
       
       try:
             s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
             s.bind(("",8888))
       except:
             sys.exit()
       try:
             d = s.recvfrom(1024)
             print("Mensaje recibido:" + d)
       except:
             sys.exit()
       
       print("Listo")

if __name__ == "__main__":
       main()
