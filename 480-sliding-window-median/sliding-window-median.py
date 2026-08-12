from bisect import bisect_left, insort

class Solution:
    def medianSlidingWindow(self, nums, k):
        window = sorted(nums[:k])
        ans = []

        for i in range(k, len(nums) + 1):

            if k % 2 == 1:
                ans.append(float(window[k // 2]))
            else:
                ans.append((window[k // 2 - 1] + window[k // 2]) / 2.0)

            if i == len(nums):
                break

            old = nums[i - k]
            idx = bisect_left(window, old)
            window.pop(idx)

            insort(window, nums[i])

        return ans
        