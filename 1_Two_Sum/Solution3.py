# execution time =  ms
# memory consumption =  MB


class Solution:
    def twoSum(self, nums, target):
        lens = len(nums)
        j = -1
        # why from 1
        for i in range(1, lens):
            temp = nums[:i]
            if (target - nums[i]) in temp:
                j = temp.index(target - nums[i])
                break
        if j > 0:
            return [i, j]


