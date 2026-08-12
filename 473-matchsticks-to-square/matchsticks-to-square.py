class Solution(object):
    def makesquare(self, matchsticks):
        total = sum(matchsticks)

        if total % 4 != 0:
            return False

        side = total // 4
        matchsticks.sort(reverse=True)
        sides = [0] * 4

        def dfs(i):
            if i == len(matchsticks):
                return True

            x = matchsticks[i]

            for j in range(4):
                if sides[j] + x <= side:
                    sides[j] += x

                    if dfs(i + 1):
                        return True

                    sides[j] -= x

                if sides[j] == 0:
                    break

            return False

        return dfs(0)
        