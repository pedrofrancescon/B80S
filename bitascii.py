class String():
    def tobits(s):
        result = []
        for c in s:
            bits = bin(ord(c))[2:]
            bits = '00000000'[len(bits):] + bits
            result.extend([int(b) for b in bits])

        nextOne = 1
        for i in range(len(result)):
            if (result[i] == -nextOne):
                result[i] = nextOne
                nextOne = -nextOne

            elif (result[i] == nextOne):
                nextOne = -nextOne

        return result

    def frombits(bits):
        chars = []
        for b in range(int(len(bits) / 8)):
            byte = bits[b*8:(b+1)*8]
            for i in range(len(byte)):
                if (byte[i] == -1):
                    byte[i] = 1
            chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
        result = ''.join(chars)
        return result
