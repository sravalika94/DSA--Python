class Solution(object):
    def findErrorNums(self, nums):
        s = set()
        dup = -1

        for x in nums:
            if x in s:
                dup = x
            s.add(x)

        miss = (len(nums) * (len(nums) + 1)) // 2 - (sum(nums) - dup)

        return [dup, miss]
        