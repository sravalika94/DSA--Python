class Solution(object):
    def calcEquation(self, equations, values, queries):
        from collections import defaultdict
        graph = defaultdict(list)

        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        def dfs(src, dst, vis):
            if src == dst:
                return 1.0
            vis.add(src)

            for nei, wt in graph[src]:
                if nei not in vis:
                    res = dfs(nei, dst, vis)
                    if res != -1:
                        return wt * res
            return -1

        ans = []
        for a, b in queries:
            if a not in graph or b not in graph:
                ans.append(-1.0)
            else:
                ans.append(dfs(a, b, set()))
        return ans
        