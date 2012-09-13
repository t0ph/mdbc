# t0ph
# Common funtions for multiple ciphers

# Remember a = 0 for ciphers
def toNum(str):
	out = []
	str = str.lower()
	x = 0
	for i in range(len(str)):
		x = ord(str[i])
		# Only A-Z are shifted.
		if ((x >= 97) & (x <= 122)):
			out.append(ord(str[i]) - 97)
	return out

#Give it an array or it freaks out!
def toLetter(num):
	out = ""
	for i in range(len(num)):
		if (num[i] < 27):
			out += chr(num[i] + 96)
		else:
			out += chr(num[i])
	return out

#Recursive modular multiplicative inverse methods lifted from
#http://numericalrecipes.blogspot.com/2009/03/modular-multiplicative-inverse.html
def extendedEuclideanAlgorithm(a, b):
	if b == 0:
		return 1,0,a
	else :
		x, y, gcd = extendedEuclideanAlgorithm(b, a % b)
		return y, x - y * (a // b),gcd

def modularInverse(a,m):
	x,y,gcd = extendedEuclideanAlgorithm(a,m)
	if gcd == 1:
		return x % m
	else:
		return None

def modMultInvAlphabet():
        for i in range(26):
                x = modularInverse(i, 26)
                print str(i) + " has an MMI of " + str(x)
