class Solution(object):
    def findDuplicate(self, paths):
        from collections import defaultdict

        mp = defaultdict(list)

        for path in paths:
            parts = path.split()

            root = parts[0]

            for file in parts[1:]:
                name, content = file.split("(")
                content = content[:-1]

                mp[content].append(root + "/" + name)

        return [v for v in mp.values() if len(v) > 1]
        