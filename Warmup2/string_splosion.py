def string_splosion(str):
	newstr = ""
	c = ""
	for i in range(len(str)):
		c = c + str[i]
		newstr = newstr + c
	return newstr
