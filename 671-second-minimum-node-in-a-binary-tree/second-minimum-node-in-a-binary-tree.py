class Solution:
    def findSecondMinimumValue(self, root):
        first = root.val
        ans = [float("inf")]

        def dfs(node):
            if not node:
                return

            if node.val > first:
                ans[0] = min(ans[0], node.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        if ans[0] == float("inf"):
            return -1

        return ans[0]