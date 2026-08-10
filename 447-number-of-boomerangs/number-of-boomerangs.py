class Solution(object):
    def numberOfBoomerangs(self, points):
        from collections import defaultdict
        ans = 0

        for i in points:
            cnt = defaultdict(int)
            for j in points:
                dx = i[0] - j[0]
                dy = i[1] - j[1]
                d = dx * dx + dy * dy
                cnt[d] += 1

            for c in cnt.values():
                ans += c * (c - 1)

        return ans
        