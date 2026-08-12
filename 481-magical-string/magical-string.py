class Solution(object):
    def magicalString(self, n):
        if n <= 0:
            return 0
        if n <= 3:
            return 1

        s = [1, 2, 2]
        i = 2
        num = 1

        while len(s) < n:
            s.extend([num] * s[i])
            num = 3 - num
            i += 1

        return s[:n].count(1)
        