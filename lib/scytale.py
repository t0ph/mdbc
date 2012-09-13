# t0ph

from common import toNum, toLetter

def encrypt(radius, plaintext):
  temp = toNum(plaintext)
  ciphertext = []
  j = 0
  while i =< radius:
    while j < plaintext
    i %= 26
    ciphertext.append(i)
  return toLetter(ciphertext)

def decrypt(shift, ciphertext):
    temp = toNum(ciphertext)
    plaintext = []
    for i in temp:
        i -= shift
        i %= 26
        plaintext.append(i)
    return toLetter(plaintext)

def bruteForce(ciphertext):
	for i in range(1,26):
		print str(i) + ": " + decrypt(i, ciphertext)
