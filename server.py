import os
from socket import *
from encryption import Crypto
from bitascii import String
from encoding import B8ZS

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
    bits = [(i-1) for i in list(received)]
    decoded = B8ZS.decode(bits)
    data = String.frombits(decoded)
    decrypted = crypto.decryptString(data)
    print("Received message: " + decrypted)
    if decrypted == "exit":
        break
    plot.ploting(decoded, data, bits, decoded, False)
UDPSock.close()
os._exit(0)
