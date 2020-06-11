# execution time = 504 ms
# memory consumption = 17.3 MB


class Solution:
    def dailyTemperatures(self, T):
        res = [0] * len(T)
        stack = []

        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                # pop the smaller value's index
                small = stack.pop()
                res[small] = i - small

            # append the index of current value
            stack.append(i)

        return res