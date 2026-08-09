"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
     
        def dfs(node):
            cur = node
            last = None

            while cur:
                nxt = cur.next

                if cur.child:
                    child_last = dfs(cur.child)

                    nxt = cur.next
                    cur.next = cur.child
                    cur.child.prev = cur
                    cur.child = None

                    if nxt:
                        child_last.next = nxt
                        nxt.prev = child_last

                    last = child_last
                else:
                    last = cur

                cur = nxt

            return last

        dfs(head)
        return head
        