#t0ph
#uses a string of.'s and -'s

from string import ascii_lowercase

#So this is the set of possible encoded letters.
#I have purposely not included non-English characters and Prosigns
#Non-English characters may be added directly, however Prosigns will require more work
key = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....", "i":"..", "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.", "q":"--.-", "r":".-.", "s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--..", "0":"-----", "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....", "6":"-....", "7":"--...", "8":"---..", "9":"----.", ".":".-.-.-", ",":"--..--", "?":"..--..", "\'":".----.", "!":"-.-.--", "/":"-..-.", "(":"-.--.", ")":"-.--.-", "&":".-...", ":":"---...", ";":"-.-.-.", "=":"-...-", "+":".-.-.", "-":"-....-", "_":"..--.-", "\"":".-..-.", "$":"...-..-", "@":".--.-."}

# 1 line of regex is easier than 6 lines of reverse lookups
dkey = {".-":"a", "-...":"b", "-.-.":"c", "-..":"d", ".":"e", "..-.":"f", "--.":"g", "....":"h", "..":"i", ".---":"j", "-.-":"k", ".-..":"l", "--":"m", "-.":"n", "---":"o", ".--.":"p", "--.-":"q", ".-.":"r", "...":"s", "-":"t", "..-":"u", "...-":"v", ".--":"w", "-..-":"x", "-.--":"y", "--..":"z", "-----":"0", ".----":"1", "..---":"2", "...--":"3", "....-":"4", ".....":"5", "-....":"6", "--...":"7", "---..":"8", "----.":"9", ".-.-.-":".", "--..--":",", "..--..":"?", ".----.":"\'", "-.-.--":"!", "-..-.":"/", "-.--.":"(", "-.--.-":")", ".-...":"&", "---...":":", "-.-.-.":";", "-...-":"=", ".-.-.":"+", "-....-":"-", "..--.-":"_", ".-..-.":"\"", "...-..-":"$", ".--.-.":"@"}

# Keeps punctuations
def simpleEncode(plaintext):
	out = ""
	temp = 0
	plaintext = plaintext.lower()
	for i in range(len(plaintext)):
		temp = ord(plaintext[i])
		if ((temp >= 97) & (temp <= 122)):
			out += key[plaintext[i]]
		else:
			out += plaintext[i]
	return out

def encode(plaintext):
        out = ""
        temp = 0
        plaintext = plaintext.lower()
        for i in range(len(plaintext)):
                if plaintext[i] in key:
                        out += key[plaintext[i]]
                else:
                        out += plaintext[i]
        return out

# If non "." or "-" characters are entered they will be preserved i.e. punctuation 
# Use any letter to indicated a space between letters
def decode(message):
        base = 0
        top = 0
        holder = ""
        plaintext = ""
        while top < len(message):
                if(message[top].isspace()):
                        for i in range(base, top):
                                holder += message[i]
                        plaintext += toLetter(holder)
                        holder = ""
                        base = top + 1
                top += 1
        for i in range(base, top):
                holder += message[i]
        plaintext += toLetter(holder)
        return plaintext

def toLetter(aLetter):
        if aLetter in dkey:
                return dkey[aLetter]
        elif aLetter.isspace():
                return ""
        elif aLetter.isalpha():
                return " "
        else:
                return aLetter


def showTable():
	x = 0
	for i in sorted(key.iterkeys()):
		x += 1
		print i + " = " + key[i] + " ",
		# Spaces for pretty formating
		if len(key[i]) == 1:
			print "  ",
		if x % 3 == 0:
			print ""
		else:
			print "\t",
	print ""

def showTableAZ():
	x = 0
	for i in ascii_lowercase:
		x += 1
                print i + " = " + key[i] + " ",
		# Spaces for pretty formating
                if len(key[i]) == 1:
                        print "  ",
                if x % 3 == 0:
                        print ""
                else:
                        print "\t",
        print ""
