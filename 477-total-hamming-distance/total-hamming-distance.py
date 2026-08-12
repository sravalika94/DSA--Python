class Solution(object):
    def totalHammingDistance(self, nums):
        ans = 0
        n = len(nums)

        for bit in range(32):
            ones = 0

            for x in nums:
                if x & (1 << bit):
                    ones += 1

            ans += ones * (n - ones)

        return ans
        