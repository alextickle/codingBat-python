def non_start(a, b):
	if len(a) == 1:
		if len(b) == 1:
			return ""
		return b[1:]
	elif len(b) == 1:
		if len(a) == 1:
			return ""
		return a[1:]
	else:
		return a[1:] + b[1:]
