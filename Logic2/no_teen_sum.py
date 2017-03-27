def no_teen_sum(a, b, c):
	sum = 0
	for i in [a, b, c]:
		if i >= 13 and i <= 19:
			sum = sum + fix_teen(i)
		else:
			sum = sum + i
	return sum
	
def fix_teen(n):
	if n == 15 or n == 16:
		return n
	else:
		return 0

