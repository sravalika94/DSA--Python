class Solution(object):
    def palindromePairs(self, words):
        def isPal(s):
            return s == s[::-1]

        mp = {w: i for i, w in enumerate(words)}
        ans = []

        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                left = word[:j]
                right = word[j:]

                if isPal(left):
                    rev = right[::-1]
                    if rev in mp and mp[rev] != i:
                        ans.append([mp[rev], i])

                if j != len(word) and isPal(right):
                    rev = left[::-1]
                    if rev in mp and mp[rev] != i:
                        ans.append([i, mp[rev]])

        return ans
        