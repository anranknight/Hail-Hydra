class Solution:
    def __init__(self):
        self.res = 0

    def sumNums(self, n):
        if n == 1:
            return 1
        n += self.sumNums(n-1)
        return n


'''    def sumNums(self, n):
        if n == 1:
            res = 1
        res = n + self.sumNums(n-1)
        print('结果是', res)
        return res'''





