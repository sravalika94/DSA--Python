class Solution(object):
    def dominantIndex(self, nums):
        largest = max(nums)
        index = nums.index(largest)

        for x in nums:
            if x != largest and largest < 2 * x:
                return -1

        return index
        