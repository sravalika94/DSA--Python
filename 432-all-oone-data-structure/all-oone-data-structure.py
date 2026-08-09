

class Node:
    def __init__(self, cnt):
        self.cnt = cnt
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.mp = {}

    def _insert(self, prev, node):
        node.next = prev.next
        node.prev = prev
        prev.next.prev = node
        prev.next = node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key):
        if key not in self.mp:
            if self.head.next == self.tail or self.head.next.cnt != 1:
                self._insert(self.head, Node(1))
            self.head.next.keys.add(key)
            self.mp[key] = self.head.next
        else:
            cur = self.mp[key]
            nxt = cur.next
            if nxt == self.tail or nxt.cnt != cur.cnt + 1:
                new = Node(cur.cnt + 1)
                self._insert(cur, new)
                nxt = new
            nxt.keys.add(key)
            self.mp[key] = nxt
            cur.keys.remove(key)
            if not cur.keys:
                self._remove(cur)

    def dec(self, key):
        if key not in self.mp:
            return

        cur = self.mp[key]

        if cur.cnt == 1:
            del self.mp[key]
        else:
            pre = cur.prev
            if pre == self.head or pre.cnt != cur.cnt - 1:
                new = Node(cur.cnt - 1)
                self._insert(pre, new)
                pre = new
            pre.keys.add(key)
            self.mp[key] = pre

        cur.keys.remove(key)
        if not cur.keys:
            self._remove(cur)

    def getMaxKey(self):
        return "" if self.tail.prev == self.head else next(iter(self.tail.prev.keys))

    def getMinKey(self):
        return "" if self.head.next == self.tail else next(iter(self.head.next.keys))
        

    


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()