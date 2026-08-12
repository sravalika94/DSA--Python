class Solution(object):
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()

        ans = 0

        for house in houses:
            left, right = 0, len(heaters) - 1

            while left <= right:
                mid = (left + right) // 2

                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid - 1

            dist1 = abs(house - heaters[right]) if right >= 0 else float('inf')
            dist2 = abs(heaters[left] - house) if left < len(heaters) else float('inf')

            ans = max(ans, min(dist1, dist2))

        return ans
        