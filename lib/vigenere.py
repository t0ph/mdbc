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
