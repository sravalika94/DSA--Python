class Solution(object):
    def findMinArrowShots(self, points):
        points.sort(key=lambda x: x[1])

        arrows = 1
        end = points[0][1]

        for s, e in points:
            if s > end:
                arrows += 1
                end = e

        return arrows
        