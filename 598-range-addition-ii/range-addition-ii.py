class Solution(object):
    def maxCount(self, m, n, ops):
        if not ops:
            return m * n

        a = min(x for x, y in ops)
        b = min(y for x, y in ops)

        return a * b
        