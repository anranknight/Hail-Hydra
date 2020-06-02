# execution time = 56 ms
# memory consumption = 21.3 MB


class Solution:
    def __init__(self):
        self.res = 0
    def sumNums(self, n):
        n > 1 and self.sumNums(n - 1)  # n = 1时就不递归了
        self.res += n
        return self.res