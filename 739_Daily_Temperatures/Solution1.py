class Solution:
    def dailyTemperatures(self, T):
        res = []
        for i in range(len(T)):
            for j in range(i+1, len(T)):
                if T[j] > T[i]:
                    res[i] = j - i
                break
        print(res)
        return res
