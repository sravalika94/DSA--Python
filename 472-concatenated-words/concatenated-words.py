class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        word_set = set(words)
        ans = []

        for word in words:
            n = len(word)
            dp = [False] * (n + 1)
            dp[0] = True

            for i in range(1, n + 1):
                for j in range(i):
                    if not dp[j]:
                        continue
                    if word[j:i] in word_set and word[j:i] != word:
                        dp[i] = True
                        break

            if dp[n]:
                ans.append(word)

        return ans
        