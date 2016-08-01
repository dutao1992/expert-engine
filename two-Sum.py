def twoSum(nums,target):
	dict = {}
	for index in xrange(0,len(nums)):
		num = nums[index]
		if num in dict:
			return [dict[num],index]
			break
		else:
			dict[target-num]=index
	print('we cannot find it')