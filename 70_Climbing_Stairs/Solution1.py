# execution time = 28 ms
# memory consumption = 13.5 MB

class Solution:
    def climbStairs(self, n):
        if n == 1:
            b = 1
        else:
            a = 1  # 1 stair
            b = 2  # 2 stairs
            for i in range(2, n):
                c = a + b
                a = b
                b = c
        return b


