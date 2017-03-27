def array_front9(nums):
	has9 = False
	if len(nums) < 4:
		r = len(nums)
	else:
		r = 4
	for i in range(r):
		if nums[i] == 9:
			has9 = True
	return has9