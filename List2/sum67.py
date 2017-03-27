def sum67(nums):
	stop = False
	sum = 0
	for i in range(len(nums)):
		if nums[i] == 6:
			stop = True
		if stop == False:
			sum = sum + nums[i]
		if nums[i] == 7:
			stop = False
	return sum
		