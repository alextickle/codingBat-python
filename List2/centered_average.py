def centered_average(nums):
	min = nums[0]
	max = nums[0]
	for i in range(len(nums)):
		if nums[i] > max:
			max = nums[i]
		if nums[i] < min:
			min = nums[i]
	sum = 0
	for j in range(len(nums)):
		sum = sum + nums[j]
	return (sum - max - min) / (len(nums) - 2)

print centered_average([1,2,3,4,5])
		
