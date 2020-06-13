class Solution:
    def threeSum(self, nums):
        res = {}
        length = len(nums)
        for i in range(length):
            for j in range(length):
                if j != i:
                    thirdnum = nums[i] + nums[j]
                    if -thirdnum in nums:
                        k = nums.index(-thirdnum)
                        if k != i and k != j:
                            tmp = [nums[i], nums[j], nums[k]]
                            tmp.sort()
                            if tmp not in res:
                                res.append(tmp)
        print(res)
        return res
