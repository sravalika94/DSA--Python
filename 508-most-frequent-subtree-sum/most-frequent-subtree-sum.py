# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findFrequentTreeSum(self, root):
        from collections import defaultdict
        cnt = defaultdict(int)

        def dfs(node):
            if not node:
                return 0

            s = node.val + dfs(node.left) + dfs(node.right)
            cnt[s] += 1
            return s

        dfs(root)

        mx = max(cnt.values())
        return [k for k, v in cnt.items() if v == mx]
        