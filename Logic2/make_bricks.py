def make_bricks(small, big, goal):
	if goal > 5 * big + small:
		return False
	else:
		if goal % 5 <= small:
			return True
		else:
			return False
