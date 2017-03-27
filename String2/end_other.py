def end_other(a, b):
	if a == b:
		return True
	elif len(a) > len(b):
		for i in range(len(b)):
			if a[-len(b) + i].lower() != b[i].lower():
				return False
		return True
	else:
		for i in range(len(a)):
			if b[-len(a) + i].lower() != a[i].lower():
				return False
		return True
	
	
