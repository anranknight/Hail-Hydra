# execution time = 64 ms
# memory consumption = 19.6 MB


class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)

        L, R, answer = [0]*length, [0]*length, [0]*length
        L[0] = 1
        for i in range(1, length): # range mean [1, length)
            L[i] = nums[i-1] * L[i-1]
        R[length-1] = 1  # range is from index 0
        # learn learn, reversed fun
        for i in reversed(range(length-1)):  # should be calculated in reverse order
            R[i] = nums[i+1] * R[i+1]

        for i in range(length):
            answer[i] = L[i] * R[i]

        return answer
