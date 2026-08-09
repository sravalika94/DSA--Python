class Solution(object):
    def originalDigits(self, s):
        from collections import Counter

        cnt = Counter(s)
        out = [0] * 10

        out[0] = cnt['z']
        out[2] = cnt['w']
        out[4] = cnt['u']
        out[6] = cnt['x']
        out[8] = cnt['g']
        out[3] = cnt['h'] - out[8]
        out[5] = cnt['f'] - out[4]
        out[7] = cnt['s'] - out[6]
        out[1] = cnt['o'] - out[0] - out[2] - out[4]
        out[9] = cnt['i'] - out[5] - out[6] - out[8]

        ans = ""
        for i in range(10):
            ans += str(i) * out[i]

        return ans
        