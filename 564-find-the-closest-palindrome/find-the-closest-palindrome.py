class Solution(object):
    def nearestPalindromic(self, n):
        l = len(n)
        num = int(n)

        cand = {
            10 ** (l - 1) - 1,
            10 ** l + 1
        }

        prefix = int(n[:(l + 1) // 2])

        for x in [prefix - 1, prefix, prefix + 1]:
            s = str(x)
            if l % 2:
                p = int(s + s[-2::-1])
            else:
                p = int(s + s[::-1])
            cand.add(p)

        cand.discard(num)

        return str(min(cand, key=lambda x: (abs(x - num), x)))