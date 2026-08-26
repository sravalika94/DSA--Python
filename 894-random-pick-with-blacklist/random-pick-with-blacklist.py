import random

class Solution:

    def __init__(self, n, blacklist):
        self.m = n - len(blacklist)
        self.mp = {}

        black = set(blacklist)
        last = n - 1

        for b in blacklist:
            if b < self.m:
                while last in black:
                    last -= 1

                self.mp[b] = last
                last -= 1

    def pick(self):
        x = random.randrange(self.m)
        return self.mp.get(x, x)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()