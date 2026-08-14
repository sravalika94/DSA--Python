class Solution(object):
    def findMinDifference(self, timePoints):
        mins = []

        for t in timePoints:
            h, m = map(int, t.split(":"))
            mins.append(h * 60 + m)

        mins.sort()
        ans = 1440 + mins[0] - mins[-1]

        for i in range(1, len(mins)):
            ans = min(ans, mins[i] - mins[i - 1])

        return ans
        