def cat_dog(str):
	countc = 0
	countd = 0
	if len(str) < 3:
		return True
	for i in range(len(str) - 2):
		if str[i] + str[i + 1] + str[i + 2] == 'dog':
			countd = countd + 1
		if str[i] + str[i + 1] + str[i + 2] == 'cat':
			countc = countc + 1
	if countc == countd:
		return True
	else:
		return False

	
