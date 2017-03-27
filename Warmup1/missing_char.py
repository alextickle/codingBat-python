def missing_char(str, n):
	newstr = ""
	count = 0
	for i in str:
		if count != n:
			newstr = newstr + i
		count = count + 1
	return newstr
