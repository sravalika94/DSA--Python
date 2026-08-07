
      

class Solution:
    def __init__(self):
        self.timer = 1  # Global timer for discovery times

    def dfs(self, node, parent, vis,
            adj, tin, low,
            bridges):
        vis[node] = 1                     # Mark as visited
        tin[node] = low[node] = self.timer  # Set discovery & low-link value
        self.timer += 1

        for neighbor in adj[node]:        # Explore neighbors
            if neighbor == parent:
                continue

            if vis[neighbor] == 0:
                # Recursive DFS call
                self.dfs(neighbor, node, vis, adj, tin, low, bridges)

                # Update low-link value
                low[node] = min(low[node], low[neighbor])

                # If the lowest reachable node from neighbor is higher than discovery time of node
                if low[neighbor] > tin[node]:
                    bridges.append([neighbor, node])
            else:
                # Back edge
                low[node] = min(low[node], low[neighbor])

    def criticalConnections(self, n, connections):
        # Step 1: Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        # Step 2: Initialize helper arrays
        vis = [0] * n
        tin = [0] * n
        low = [0] * n
        bridges = []

        # Step 3: Run DFS
        self.dfs(0, -1, vis, adj, tin, low, bridges)
        return bridges


        