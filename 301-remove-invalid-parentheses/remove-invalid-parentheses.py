class Solution(object):
    def removeInvalidParentheses(self, s):
        from collections import deque
        def isValid(string):
            count = 0
            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        res = []
        visited = set([s])
        q = deque([s])
        found = False

        while q:
            cur = q.popleft()

            if isValid(cur):
                res.append(cur)
                found = True

            if found:
                continue

            for i in range(len(cur)):
                if cur[i] not in "()":
                    continue

                nxt = cur[:i] + cur[i + 1:]

                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)

        return res
        