def make_ends(nums):
	if len(nums) == 1:
		return nums + [nums[0]]
	else:
		return [nums[0]] + [nums[-1]]
