class Solution(object):
    def wiggleSort(self, nums):
        temp = sorted(nums)
        n = len(nums)

        left = (n - 1) // 2
        right = n - 1

        for i in range(n):
            if i % 2 == 0:
                nums[i] = temp[left]
                left -= 1
            else:
                nums[i] = temp[right]
                right -= 1
        