class Solution(object):
    def smallestDistancePair(self, nums, k):
        nums.sort()

        left = 0
        right = nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2
            count = 0
            j = 0

            for i in range(len(nums)):
                while nums[i] - nums[j] > mid:
                    j += 1

                count += i - j

            if count >= k:
                right = mid
            else:
                left = mid + 1

        return left
        