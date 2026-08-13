import random
class Solution(object):

    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.total = m * n
        self.mp = {}

    def flip(self):
        r = random.randint(0, self.total - 1)
        self.total -= 1

        x = self.mp.get(r, r)
        self.mp[r] = self.mp.get(self.total, self.total)

        return [x // self.n, x % self.n]

    def reset(self):
        self.total = self.m * self.n
        self.mp.clear()
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()