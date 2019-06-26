import base64

class B8ZS():
    
    def encode(bits):
    	zeroCount = 0
    	lastOne = -1

    	for i in range(len(bits)):
    		
    		if (bits[i] == 0):
    			zeroCount += 1
    		else:
    			zeroCount = 0
    			lastOne = bits[i]

    		if (zeroCount == 8):
    			zeroCount = 0

    			bits[i] = lastOne
    			bits[i-1] = -lastOne
    			bits[i-2] = 0
    			bits[i-3] = -lastOne
    			bits[i-4] = lastOne
    			bits[i-5] = 0
    			bits[i-6] = 0
    			bits[i-7] = 0

    	return bits
    			

    def decode(bits):
    	lastOne = 0

    	for i in range(len(bits)):
    		
    		if (bits[i] != 0):
    			
    			if (bits[i] == lastOne):
    				
    				lastOne = bits[i]
    				
    				bits[i-3] = 0
    				bits[i-2] = 0
    				bits[i-1] = 0
    				bits[i] = 0
    				bits[i+1] = 0
    				bits[i+2] = 0
    				bits[i+3] = 0
    				bits[i+4] = 0

    			else:
    				lastOne = bits[i]

    	return bits
