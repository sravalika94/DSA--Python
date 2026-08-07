class Solution(object):
    def firstUniqChar(self, s):
        from collections import Counter
        cnt = Counter(s)

        for i, ch in enumerate(s):
            if cnt[ch] == 1:
                return i

        return -1
        