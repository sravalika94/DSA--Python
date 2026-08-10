class Codec:

    def serialize(self, root):
        vals = []

        def preorder(node):
            if not node:
                return
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(vals)

    def deserialize(self, data):
        if not data:
            return None

        vals = list(map(int, data.split(",")))
        self.idx = 0

        def build(low, high):
            if self.idx == len(vals):
                return None

            val = vals[self.idx]
            if val <= low or val >= high:
                return None

            self.idx += 1
            node = TreeNode(val)
            node.left = build(low, val)
            node.right = build(val, high)
            return node

        return build(float("-inf"), float("inf"))