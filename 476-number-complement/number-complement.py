class Solution(object):
    def findComplement(self, num):
        mask = 1

        while mask <= num:
            mask <<= 1

        mask -= 1

        return num ^ mask
        