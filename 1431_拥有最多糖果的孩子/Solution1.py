# execution time = 44 ms
# memory consumption = 13.7 MB

class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maxCandies = max(candies)
        ret = [candy + extraCandies >= maxCandies for candy in candies]
        return ret
