class Solution(object):
    def getHint(self, secret, guess):
        from collections import Counter
        bulls = 0
        s = Counter()
        g = Counter()

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                s[secret[i]] += 1
                g[guess[i]] += 1

        cows = 0
        for ch in s:
            cows += min(s[ch], g[ch])

        return str(bulls) + "A" + str(cows) + "B"
        