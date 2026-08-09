class Solution(object):
    def longestPalindrome(self, s):
        from collections import Counter

        cnt = Counter(s)
        ans = 0
        odd = False

        for v in cnt.values():
            if v % 2 == 0:
                ans += v
            else:
                ans += v - 1
                odd = True

        return ans + 1 if odd else ans
        