#t0ph
#Affine cipher

from common import toNum, toLetter, modularInverse

def encrypt(alpha, beta, plaintext):
	ciphertext = toNum(plaintext)
	for i in range(len(ciphertext)):
		if plaintext[i].isalpha():
			ciphertext[i] = (ciphertext[i] * alpha + beta) % 26
	return toLetter(ciphertext)

def decrypt(alpha, beta, ciphertext):
	modInv = modularInverse(alpha, 26)
	if modInv != None:
		plaintext = toNum(ciphertext)
		for i in range(len(plaintext)):
			if ciphertext[i].isalpha():
				plaintext[i] = (modInv*(plaintext[i]-beta)) % 26
		return toLetter(plaintext)
	else:
		return "No MMI for " + str(alpha) + " and 26."

def bruteForce(ciphertext):
	# These are the only possible alphas as these are the only numbers
	# that have modular multiplicative inverses with 26
	alphas = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
	betas = range(26)
	i = 1
	for x in alphas:
		for y in betas:
			print "#" + str(i) + ": " + decrypt(x, y, ciphertext)
			i += 1
