#t0ph

import sys, os
cwd = os.getcwd()
cwd += "/lib"
sys.path.append(cwd)
import common, shift, morse, atbash, affine, vigenere

def makeItRain(ciphertext):
	print "Cry \'Havoc!\', and let slip the dogs of war"
	print "Shift Cipher:"
	shift.bruteForce(ciphertext)
	print "\nAffine Cipher:"
	affine.bruteForce(ciphertext)
	print "\nAtbash :"
	print atbash.decrypt(ciphertext)
	print "\nMorse Code:"
	print morse.encode(ciphertext)
