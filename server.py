import os
from socket import *
host = ""
port = 13000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)

def frombits(bits):
    chars = []
    for b in range(int(len(bits) / 8)):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(byte,2)))
    return ''.join(chars)

print("Waiting to receive messages...")
while True:
    (received, addr) = UDPSock.recvfrom(buf)

    bits = received.decode()

    # executar algorítmo de decodificação em 'bits'

    data = frombits(bits)

    print("Received message: " + data)
    if data == "exit":
        break
UDPSock.close()
os._exit(0)