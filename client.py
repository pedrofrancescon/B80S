import os
from socket import *
from encryption import Crypto
from bitascii import String
from encoding import B8ZS

host = "10.183.7.141"
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)

crypto = Crypto('senha')

# test = [1,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1,-1]
# print(test)
# encoded = B8ZS.encode(test)
# print(encoded)
# decoded = B8ZS.decode(encoded)
# print(decoded)

while True:
    data = input("Enter message to send or type 'exit': ")
    encrypted = crypto.encryptString(data)
    bits = String.tobits(encrypted)
    encoded = B8ZS.encode(bits)
    UDPSock.sendto(bytes([(i+1) for i in encoded]), addr)
    if data == "exit":
        print("Aplicação encerrada!")
        break
UDPSock.close()
os._exit(0)
