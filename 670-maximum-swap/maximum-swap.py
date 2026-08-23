class Solution(object):
    def maximumSwap(self, num):
        nums = list(str(num))
        last = {}

        for i in range(len(nums)):
            last[int(nums[i])] = i

        for i in range(len(nums)):
            for d in range(9, int(nums[i]), -1):
                if d in last and last[d] > i:
                    j = last[d]
                    nums[i], nums[j] = nums[j], nums[i]
                    return int("".join(nums))

        return num
        