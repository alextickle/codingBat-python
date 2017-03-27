def combo_string(a, b):
	if a == "":
		return b
	elif b == "":
		return a
	else:
		if len(a) > len(b):
			return b + a + b
		else:
			return a + b + a