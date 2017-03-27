def front3(str):
	if len(str) < 3:
		front = str
	else:
		front = str[0] + str[1] + str[2]
	return front * 3
