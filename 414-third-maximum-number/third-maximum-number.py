class Solution(object):
    def thirdMax(self, nums):
        s = set(nums)

        if len(s) < 3:
            return max(s)

        s.remove(max(s))
        s.remove(max(s))

        return max(s)
        