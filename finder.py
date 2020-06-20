from socket import *
import sys

HOST = ''
PORT = 5008
PORT_IN = 5009
ADDRESS = "255.255.255.255"

s =socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
s.bind((HOST, PORT_IN))

while True:
    msg = input("> ")
    s.sendto(msg.encode(), (ADDRESS, PORT))
    if msg == ".":
        break
    msg, address = s.recvfrom(64)
    print("message:", msg, "from", address)

s.close()
sys.exit()
