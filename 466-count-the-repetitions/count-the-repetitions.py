class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        if not set(s2).issubset(set(s1)):
            return 0

        recall = {}
        s1cnt = s2cnt = idx = 0

        while s1cnt < n1:
            for ch in s1:
                if ch == s2[idx]:
                    idx += 1
                    if idx == len(s2):
                        idx = 0
                        s2cnt += 1

            s1cnt += 1

            if idx in recall:
                pre_s1, pre_s2 = recall[idx]
                cycle_s1 = s1cnt - pre_s1
                cycle_s2 = s2cnt - pre_s2

                remain = n1 - s1cnt
                times = remain // cycle_s1

                s1cnt += times * cycle_s1
                s2cnt += times * cycle_s2
            else:
                recall[idx] = (s1cnt, s2cnt)

        return s2cnt // n2
        