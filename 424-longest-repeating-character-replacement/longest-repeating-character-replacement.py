class Solution(object):
    def characterReplacement(self, s, k):
        from collections import defaultdict
        cnt = defaultdict(int)
        left = 0
        best = 0
        ans = 0

        for right in range(len(s)):
            cnt[s[right]] += 1
            best = max(best, cnt[s[right]])

            while (right - left + 1) - best > k:
                cnt[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
        