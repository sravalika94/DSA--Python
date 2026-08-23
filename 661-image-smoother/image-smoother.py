class Solution(object):
    def imageSmoother(self, img):
        m = len(img)
        n = len(img[0])
        ans = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                total = 0
                count = 0

                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        ni = i + di
                        nj = j + dj

                        if 0 <= ni < m and 0 <= nj < n:
                            total += img[ni][nj]
                            count += 1

                ans[i][j] = total // count

        return ans
        