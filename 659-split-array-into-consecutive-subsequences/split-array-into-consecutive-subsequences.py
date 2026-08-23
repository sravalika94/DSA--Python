class Solution(object):
    def isPossible(self, nums):
        from collections import Counter, defaultdict

        freq = Counter(nums)
        end = defaultdict(int)

        for x in nums:
            if freq[x] == 0:
                continue

            freq[x] -= 1

            if end[x - 1] > 0:
                end[x - 1] -= 1
                end[x] += 1

            elif freq[x + 1] > 0 and freq[x + 2] > 0:
                freq[x + 1] -= 1
                freq[x + 2] -= 1
                end[x + 2] += 1

            else:
                return False

        return True
        