class Solution(object):
    def arrayNesting(self, nums):
        vis = [False] * len(nums)
        ans = 0

        for i in range(len(nums)):
            if vis[i]:
                continue

            cnt = 0
            while not vis[i]:
                vis[i] = True
                i = nums[i]
                cnt += 1

            ans = max(ans, cnt)

        return ans
        