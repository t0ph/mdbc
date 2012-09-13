import string
import shift

atoz = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def generateKey(key):
	hkey = key.lower()
	hkey = hkey.replace(' ', '')
	holder = hkey[0]
	contains = False
	for i in range(len(hkey)):
		contains = False
		for j in range(len(holder)):
			if holder[j] == hkey[i]:
				contains = True
		if contains == False:
			holder = holder + hkey[i]
	for l in range(len(atoz)):
                contains = False
                for m in range(len(holder)):
                        if holder[m] == atoz[l]:
                                contains = True
                if contains == False:
                        holder = holder + atoz[l]
	return holder

def encrypt(plaintext, key):
	hkey = generateKey(key)
	nplaintext = plaintext.lower()
	translation_table = string.maketrans(string.ascii_lowercase, hkey)
	out = plaintext.translate(translation_table)
	return out

def speedy(plaintext, key):
	w = encrypt(plaintext, key)
	shift.bruteForce(w)