def xyz_there(str):
	if len(str) < 3:
		return False
	elif len(str) == 3:
		if str == 'xyz':
			return True
		else:
			return False
	else:	
		if str[:3] == 'xyz':
			return True
		for i in range(len(str) - 3):
			if str[i + 1] + str[i + 2] + str[i + 3] == 'xyz' and str[i] != '.':
				return True
		return False
			
