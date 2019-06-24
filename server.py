import os
from socket import *
from encryption import Crypto
from bitascii import String

host = ""
port = 13000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)

crypto = Crypto('senha')

print("Waiting to receive messages...")
while True:
    (received, addr) = UDPSock.recvfrom(buf)
    bits = received.decode()

    # executar algorítmo de decodificação em 'bits'

    data = String.frombits(bits)
    decrypted = crypto.decryptString(data)
    print("Received message: " + decrypted)
    if decrypted == "exit":
        break
UDPSock.close()
os._exit(0)