#t0ph
#

from common import toNum, toLetter

#Saves punctuation.
def encrypt(key, plaintext):
	ciphertext = []
	sanitizedKey = sanitizeKey(key)
	numPlaintext = toNum(plaintext)
	y = 0 #key index
	for x in range(len(plaintext)):
		if plaintext[x].isalpha():
			ciphertext.append((numPlaintext[x] + sanitizedKey[y])%26)
			y = (y +1)%len(sanitizedKey)
		else:
			ciphertext.append(plainttext[x])
	return toLetter(ciphertext)

def decrypt(key, ciphertext):
	plaintext = []
        sanitizedKey = sanitizeKey(key)
        numCiphertext = toNum(ciphertext)
        y = 0 #key index
        for x in range(len(ciphertext)):
                if ciphertext[x].isalpha():
                        plaintext.append((numCiphertext[x] - sanitizedKey[y])%26)
                        y = (y +1)%len(sanitizedKey)
                else:
                        plaintext.append(ciphertext[x])
	return toLetter(plaintext)

def sanitizeKey(key):
	sanitizedKey = ''
	for y in range(len(key)):
                if key[y].isalpha():
                        sanitizedKey += key[y]
        sanitizedKey = toNum(sanitizedKey)
	return sanitizedKey

def simpleKnownPlaintextAttack(knownText, ciphertext): 
    for i in range(len(ciphertext)):
    	print '.'*i,
    	print decrypt(knownText, ciphertext[i:i+len(knownText)]),
    	print '.'*(len(ciphertext)-(i+len(knownText)))

def knownPlaintextAttack(knownText, ciphertext): 
    key = knownText.upper()
    out = ''
    outz = ''
    for i in range(len(knownText)):
    	outz = ''
    	if i:
    		key = 'a'+key
    	out = decrypt(key,ciphertext)
    	for x in range(len(out)):
    		if x % (len(key)) < i:
    			outz = outz+'.'
    		else:
    			outz = outz + out[x]
    	print outz
    	print makeKey(key,ciphertext)
    	print ''

def makeKey(key, ciphertext):
	i=0
	icon = True
	out = ''
	while icon:
		if len(out) == len(ciphertext):
			icon = False
		else:
			out = out + key[i]
			i = (i+1)%len(key)
	return out