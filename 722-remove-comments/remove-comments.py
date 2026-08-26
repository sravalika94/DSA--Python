class Solution(object):
    def removeComments(self, source):
        ans = []
        block = False
        cur = ""

        for line in source:
            i = 0

            while i < len(line):
                if not block and i + 1 < len(line) and line[i:i+2] == "//":
                    break

                if not block and i + 1 < len(line) and line[i:i+2] == "/*":
                    block = True
                    i += 2
                    continue

                if block and i + 1 < len(line) and line[i:i+2] == "*/":
                    block = False
                    i += 2
                    continue

                if not block:
                    cur += line[i]

                i += 1

            if not block and cur:
                ans.append(cur)
                cur = ""

        return ans
        