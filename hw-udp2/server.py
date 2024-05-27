from socket import *
import random

port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    data, addr = sock.recvfrom(BUFF_SIZE)
    if random.random() <= 0.5:
        continue
    else:
        sock.sendto(b'ack', addr)
        print('<-', data.decode())
        