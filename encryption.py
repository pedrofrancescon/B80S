import base64

class Crypto():
    def __init__(self, password):
        # senha utilizada na criptografia
        self.password = password
        return

    def encryptString(self, string):
        enc = []
        for i in range(len(string)):
            key_c = self.password[i % len(self.password)]
            enc_c = chr((ord(string[i]) + ord(key_c)) % 256)
            enc.append(enc_c)
        
        return base64.urlsafe_b64encode("".join(enc).encode()).decode()

        
    def decryptString(self, string):
        dec = []
        string = base64.urlsafe_b64decode(string).decode()
        for i in range(len(string)):
            key_c = self.password[i % len(self.password)]
            dec_c = chr((256 + ord(string[i]) - ord(key_c)) % 256)
            dec.append(dec_c)
        
        return "".join(dec)
