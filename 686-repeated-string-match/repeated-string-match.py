class Solution:
    def repeatedStringMatch(self, a, b):
        s = ""
        count = 0

        while len(s) < len(b):
            s += a
            count += 1

        if b in s:
            return count

        if b in s + a:
            return count + 1

        return -1