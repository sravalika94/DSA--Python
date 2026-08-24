class Solution(object):
    def judgePoint24(self, cards):

        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6

            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):

                    a = nums[i]
                    b = nums[j]

                    rest = [
                        nums[k] for k in range(len(nums))
                        if k != i and k != j
                    ]

                    values = [
                        a + b,
                        a - b,
                        b - a,
                        a * b
                    ]

                    if abs(b) > 1e-6:
                        values.append(a / b)

                    if abs(a) > 1e-6:
                        values.append(b / a)

                    for x in values:
                        if dfs(rest + [x]):
                            return True

            return False

        return dfs([float(x) for x in cards])
        