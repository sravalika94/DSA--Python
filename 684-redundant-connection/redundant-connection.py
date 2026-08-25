class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)
        parent = list(range(n + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in edges:
            pa = find(a)
            pb = find(b)

            if pa == pb:
                return [a, b]

            parent[pa] = pb