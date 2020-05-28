def twoSum(nums, target):
    lens = len(nums)
    j = -1
    for i in range(lens):
        # 判断第二个整数是否在数组中
        if target - nums[i] in nums:
            # 判断是否找到的就是第一个整数，如果是则跳出循环
            if (nums.count(target - nums[i]) == 1) & (target - nums[i] == nums[i]):
                continue
            else:
                # 获取第二个整数的位置
                j = nums.index(target - nums[i], i+1)
                break
    if j > 0:
        return [i, j]
    else:
        return[]

