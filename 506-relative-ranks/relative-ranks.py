class Solution(object):
    def findRelativeRanks(self, score):
        order = sorted(range(len(score)), key=lambda i: -score[i])
        ans = [""] * len(score)

        for i, idx in enumerate(order):
            if i == 0:
                ans[idx] = "Gold Medal"
            elif i == 1:
                ans[idx] = "Silver Medal"
            elif i == 2:
                ans[idx] = "Bronze Medal"
            else:
                ans[idx] = str(i + 1)

        return ans
        