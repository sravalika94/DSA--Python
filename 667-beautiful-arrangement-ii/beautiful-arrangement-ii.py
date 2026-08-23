class Solution(object):
    def constructArray(self, n, k):
        ans = []

        left = 1
        right = n

        while left <= right:
            if k > 1:
                if k % 2 == 1:
                    ans.append(left)
                    left += 1
                else:
                    ans.append(right)
                    right -= 1

                k -= 1
            else:
                ans.append(left)
                left += 1

        return ans
        