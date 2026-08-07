class Solution(object):
    def longestSubstring(self, s, k):
        from collections import Counter
        if len(s) < k:
            return 0

        cnt = Counter(s)

        for ch in cnt:
            if cnt[ch] < k:
                return max(
                    self.longestSubstring(part, k)
                    for part in s.split(ch)
                )

        return len(s)
        