from collections import defaultdict

class Solution:
    def findDuplicateSubtrees(self, root):
        count = defaultdict(int)
        ids = {}
        ans = []
        next_id = [1]

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            key = (node.val, left, right)

            if key not in ids:
                ids[key] = next_id[0]
                next_id[0] += 1

            uid = ids[key]
            count[uid] += 1

            if count[uid] == 2:
                ans.append(node)

            return uid

        dfs(root)
        return ans