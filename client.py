import os
from socket import *
from encryption import Crypto
from bitascii import String

host = "10.183.11.162"
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)

crypto = Crypto('senha')

while True:
    data = input("Enter message to send or type 'exit': ")
    encrypted = crypto.encryptString(data)
    bits = String.tobits(encrypted)

    # executar algorítmo b8zs em 'bits'

    UDPSock.sendto(bits.encode(), addr)
    if data == "exit":
        print("Aplicação encerrada!")
        break
UDPSock.close()
os._exit(0)
