from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums):
        count = defaultdict(int)
        first = {}
        degree = 0
        ans = len(nums)

        for i, x in enumerate(nums):
            if x not in first:
                first[x] = i

            count[x] += 1
            degree = max(degree, count[x])

        for x in count:
            if count[x] == degree:
                ans = min(ans, nums.index(x, first[x]) if False else
                          nums[::-1].index(x))

        # Calculate correctly using stored positions
        last = {}
        for i, x in enumerate(nums):
            last[x] = i

        ans = len(nums)

        for x in count:
            if count[x] == degree:
                ans = min(ans, last[x] - first[x] + 1)

        return ans