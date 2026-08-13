class Solution(object):
    def checkSubarraySum(self, nums, k):
        mp = {0: -1}
        s = 0

        for i, x in enumerate(nums):
            s += x
            if k:
                s %= k

            if s in mp:
                if i - mp[s] > 1:
                    return True
            else:
                mp[s] = i

        return False
        