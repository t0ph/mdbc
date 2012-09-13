def letterToPhone(text):
	out = ''
	rext = text.lower()
	for i in range(len(text)):
		if rext[i] == 'a' or rext[i] == 'b' or rext[i] == 'c':
			out = out + '2'
		if rext[i] == 'd' or rext[i] == 'e' or rext[i] == 'f':
			out = out + '3'
		if rext[i] == 'g' or rext[i] == 'h' or rext[i] == 'i':
			out = out + '4'
		if rext[i] == 'j' or rext[i] == 'k' or rext[i] == 'l':
			out = out + '5'
		if rext[i] == 'm' or rext[i] == 'n' or rext[i] == 'o':
			out = out + '6'
		if rext[i] == 'p' or rext[i] == 'q' or rext[i] == 'r' or rext[i] =='s':
			out = out + '7'
		if rext[i] == 't' or rext[i] == 'u' or rext[i] == 'v':
			out = out + '8'
		if rext[i] == 'w' or rext[i] == 'x' or rext[i] == 'y' or rext[i] =='z':
			out = out + '9'
	return out