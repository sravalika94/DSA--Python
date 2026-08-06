class Solution(object):
    def findRightInterval(self, intervals):
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        ans = []

        for start, end in intervals:
            l, r = 0, len(starts)
            while l < r:
                mid = (l + r) // 2
                if starts[mid][0] < end:
                    l = mid + 1
                else:
                    r = mid

            if l == len(starts):
                ans.append(-1)
            else:
                ans.append(starts[l][1])

        return ans
        