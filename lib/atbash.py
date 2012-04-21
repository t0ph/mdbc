#t0ph
# Atbash is equivilant to Affine with an alpha and beta of 25, otherwise
# abcdefghijklmnopqrstuvwxyz
# zyxwvutsrqponmlkjihgfedcba
# For Atbash encrypting = decrypting

import affine

def encrypt(plaintext):
	return affine.encrypt(25, 25, plaintext)

def decrypt(ciphertext):
        return affine.decrypt(25, 25, ciphertext)
