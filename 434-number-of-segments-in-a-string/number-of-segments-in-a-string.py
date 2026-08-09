class Solution(object):
    def countSegments(self, s):
        ans = 0

        for i in range(len(s)):
            if s[i] != ' ' and (i == 0 or s[i - 1] == ' '):
                ans += 1

        return ans
        