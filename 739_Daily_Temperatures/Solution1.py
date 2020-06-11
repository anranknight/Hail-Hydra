# out of time


class Solution:
    def dailyTemperatures(self, T):
        l = len(T)
        res = [0] * l
        for i in range(l):
            for j in range(i+1, l):
                if T[j] > T[i]:
                    res[i] = j - i
                    break

        print(res)
        return res
