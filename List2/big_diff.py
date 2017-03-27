def big_diff(nums):
	min = nums[0]
	max = nums[0]
	for i in nums:
		if i > max:
			max = i
		if i < min:
			min = i
	return max - min
