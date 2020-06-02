# 超出时间限制


class Solution:
    def twoSum(self, nums, target):
        lens = len(nums)
        for i in range(lens):
            for j in range(lens):
                if (nums[i] + nums[j] == target) & (i != j):
                    # return自行跳出循环
                    return [i, j]

