class Solution:
    def sumNums(self, n):
        res = 0
        for i in range(1, n+1): # 注意括号是左闭右开的
            res += i
        print('结果是', res)
        return res