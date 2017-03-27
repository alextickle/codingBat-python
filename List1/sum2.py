def sum2(nums):
	sum = 0
	if len(nums) < 2:
		for i in nums:
			sum = sum + i
	else:
		sum = nums[0] + nums[1]
	return sum
			
