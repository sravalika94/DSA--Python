# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        prefix = {0: 1}

        def dfs(node, curr):
            if not node:
                return 0

            curr += node.val
            ans = prefix.get(curr - targetSum, 0)

            prefix[curr] = prefix.get(curr, 0) + 1

            ans += dfs(node.left, curr)
            ans += dfs(node.right, curr)

            prefix[curr] -= 1

            return ans

        return dfs(root, 0)
        