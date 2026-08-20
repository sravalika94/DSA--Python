class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        cnt = 0

        for i in range(len(flowerbed)):
            if (flowerbed[i] == 0 and
                (i == 0 or flowerbed[i - 1] == 0) and
                (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)):

                flowerbed[i] = 1
                cnt += 1

        return cnt >= n
        