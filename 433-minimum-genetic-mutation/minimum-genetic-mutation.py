class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        from collections import deque
        bank = set(bank)

        if endGene not in bank:
            return -1

        q = deque([(startGene, 0)])
        vis = {startGene}
        genes = "ACGT"

        while q:
            gene, step = q.popleft()

            if gene == endGene:
                return step

            arr = list(gene)

            for i in range(8):
                old = arr[i]

                for ch in genes:
                    if ch == old:
                        continue

                    arr[i] = ch
                    nxt = "".join(arr)

                    if nxt in bank and nxt not in vis:
                        vis.add(nxt)
                        q.append((nxt, step + 1))

                arr[i] = old

        return -1
        