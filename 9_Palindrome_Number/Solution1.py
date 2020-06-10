# execution time = 76 ms
# memory consumption = 13.8 MB 果然内存消耗比较大

class Solution:
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]
