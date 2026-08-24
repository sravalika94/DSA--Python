class MapSum:

    def __init__(self):
        self.mp = {}

    def insert(self, key, val):
        self.mp[key] = val

    def sum(self, prefix):
        ans = 0

        for key in self.mp:
            if key.startswith(prefix):
                ans += self.mp[key]

        return ans