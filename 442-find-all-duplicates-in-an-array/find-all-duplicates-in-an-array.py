class Solution(object):
    def findDuplicates(self, nums):
        ans = []

        for x in nums:
            idx = abs(x) - 1
            if nums[idx] < 0:
                ans.append(abs(x))
            else:
                nums[idx] *= -1

        return ans
        