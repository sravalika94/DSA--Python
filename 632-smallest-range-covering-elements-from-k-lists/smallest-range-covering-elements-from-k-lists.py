class Solution(object):
    def smallestRange(self, nums):
        import heapq
        heap = []
        mx = float("-inf")

        for i, row in enumerate(nums):
            heapq.heappush(heap, (row[0], i, 0))
            mx = max(mx, row[0])

        ans = [-10**5, 10**5]

        while True:
            mn, r, c = heapq.heappop(heap)

            if mx - mn < ans[1] - ans[0]:
                ans = [mn, mx]

            if c + 1 == len(nums[r]):
                break

            nxt = nums[r][c + 1]
            mx = max(mx, nxt)
            heapq.heappush(heap, (nxt, r, c + 1))

        return ans
        