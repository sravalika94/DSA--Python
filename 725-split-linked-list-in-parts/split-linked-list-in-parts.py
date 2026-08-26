# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        n = 0
        curr = head

        while curr:
            n += 1
            curr = curr.next

        size = n // k
        extra = n % k

        ans = []
        curr = head

        for i in range(k):
            part_size = size + (1 if i < extra else 0)

            if part_size == 0:
                ans.append(None)
                continue

            part_head = curr

            for _ in range(part_size - 1):
                curr = curr.next

            next_part = curr.next
            curr.next = None
            curr = next_part

            ans.append(part_head)

        return ans
        