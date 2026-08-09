class Solution(object):
    def pacificAtlantic(self, heights):
        if not heights:
            return []

        m, n = len(heights), len(heights[0])
        pac = set()
        atl = set()

        def dfs(r, c, vis):
            vis.add((r, c))
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0 <= nc < n and
                    (nr, nc) not in vis and
                    heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, vis)

        for i in range(m):
            dfs(i, 0, pac)
            dfs(i, n - 1, atl)

        for j in range(n):
            dfs(0, j, pac)
            dfs(m - 1, j, atl)

        return list(pac & atl)
        