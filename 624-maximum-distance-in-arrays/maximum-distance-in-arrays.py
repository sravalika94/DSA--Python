class Solution(object):
    def maxDistance(self, arrays):
        ans = 0
        mn = arrays[0][0]
        mx = arrays[0][-1]

        for arr in arrays[1:]:
            ans = max(ans,
                      abs(arr[-1] - mn),
                      abs(mx - arr[0]))

            mn = min(mn, arr[0])
            mx = max(mx, arr[-1])

        return ans
        