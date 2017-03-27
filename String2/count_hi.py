def count_hi(str):
	if len(str) < 2:
		return 0
	count = 0
	for i in range(len(str) - 1):
		if str[i] + str[i + 1] == 'hi':
			count = count + 1
	return count