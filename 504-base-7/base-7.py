class Solution(object):
    def convertToBase7(self, num):
        if num == 0:
            return "0"

        sign = ""
        if num < 0:
            sign = "-"
            num = -num

        ans = []

        while num:
            ans.append(str(num % 7))
            num //= 7

        return sign + "".join(ans[::-1])
        