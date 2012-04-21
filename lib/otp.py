#t0ph
#It's like vigenere, but it bitches at you!
#Why yes, it is a waste of memory!

import vigenere

def encrypt(key, plaintext):
	if len(key) < len(plaintext):
		return "The key needs to be longer, son."
	else:
		return vigenere.encrypt(key, plaintext)

def decrypt(key, ciphertext):
	if len(key) < len(ciphertext):
		return "The key needs to be longer, son."
        else:
                return vigenere.decrypt(key, ciphertext)
