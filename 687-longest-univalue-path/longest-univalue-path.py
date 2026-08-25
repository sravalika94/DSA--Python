# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root):
        ans = [0]

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            l = 0
            r = 0

            if node.left and node.left.val == node.val:
                l = left + 1

            if node.right and node.right.val == node.val:
                r = right + 1

            ans[0] = max(ans[0], l + r)

            return max(l, r)

        dfs(root)
        return ans[0]
        