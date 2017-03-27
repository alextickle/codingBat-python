def sum13(nums):
	if nums == []:
		return 0
	sum = 0
	to_subtract = 0
	for i in range(len(nums) - 1):
		if nums[i] == 13:
			to_subtract = to_subtract + 13 + nums[i + 1]
		sum = sum + nums[i]
	if nums[-1] == 13:
		sum = sum - to_subtract
	else:
		sum = sum + nums[-1] - to_subtract
	if sum < 0:
		sum = 0
	return sum

print sum13([1,2,3,4,5,6])