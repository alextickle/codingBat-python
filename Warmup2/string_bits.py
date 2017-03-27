def string_bits(str):
	newstr = ""
	count = 0
	while count < len(str):
		newstr = newstr + str[count]
		count = count + 2
	return newstr
		
