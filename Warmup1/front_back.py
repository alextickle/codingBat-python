def front_back(str):
	newstr = str[-1]
	for i in range(len(str) - 2):
		newstr = newstr + str[i + 1]
	newstr = newstr + str[0] 
	return newstr

print front_back("hello")
