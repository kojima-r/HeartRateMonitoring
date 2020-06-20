from socket import *
import sys
import netifaces

HOST = ''   
ECHO_PORT = 5008

myaddr=netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']

s =socket(AF_INET,SOCK_DGRAM)
s.bind((HOST, ECHO_PORT))

while(True):
    msg, address = s.recvfrom(64)
    if msg[0] == ".":
        print("Sender is closed")
        break
    print("message:", msg, "from", address)
    s.sendto(myaddr.encode(),address)
s.close()
sys.exit()

