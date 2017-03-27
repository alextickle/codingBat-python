def not_string(str):
	if len(str) < 3:
		return "not " + str
	elif "not" == str[0] + str[1] + str[2]:
		return str
	else:
		return "not " + str
		
		