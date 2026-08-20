class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        def dist(a, b):
            return (a[0]-b[0])**2 + (a[1]-b[1])**2

        d = sorted([
            dist(p1, p2), dist(p1, p3), dist(p1, p4),
            dist(p2, p3), dist(p2, p4), dist(p3, p4)
        ])

        return d[0] > 0 and d[0] == d[3] and d[4] == d[5]
        