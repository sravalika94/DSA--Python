from collections import Counter

class Solution:
    def topKFrequent(self, words, k):
        count = Counter(words)

        arr = list(count.keys())
        arr.sort(key=lambda x: (-count[x], x))

        return arr[:k]
        