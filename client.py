import os
from socket import *
host = "192.168.0.104"
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)

def tobits(s):
    result = ''
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result += bits
    return result

while True:
    data = input("Enter message to send or type 'exit': ")
    bits = tobits(data)
    # executar algorítmo b8zs em 'bits'
    UDPSock.sendto(bits.encode(), addr)
    if data == "exit":
        print("Aplicação encerrada!")
        break
UDPSock.close()
os._exit(0)
