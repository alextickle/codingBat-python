def make_chocolate(small, big, goal):
	if goal > 5 * big + small:
		return -1
	else:
		if goal % 5 <= small:
			if big * 5 >= goal:
				return goal % 5
			else:
				return goal - (big * 5)
		else:
			return -1
