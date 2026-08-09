"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        from collections import deque
        if not root:
            return []

        q = deque([root])
        ans = []

        while q:
            level = []

            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                for child in node.children:
                    q.append(child)

            ans.append(level)

        return ans
        