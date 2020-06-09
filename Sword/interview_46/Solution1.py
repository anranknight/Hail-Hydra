# execution time = 40 ms
# memory consumption = 13.6 MB


class Solution:
    def translateNum(self, num):
        s = str(num)
        a = b = 1  # 取了0和1情况下的初始值，按a b c的顺序
        for i in range(2, len(s)+1):
            c = a + b if '10' <= s[i-2:i] <= '25' else b
            a = b
            b = c
        return b




