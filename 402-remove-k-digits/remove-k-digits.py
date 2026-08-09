class Solution(object):
    def removeKdigits(self, num, k):
        st = []

        for ch in num:
            while k and st and st[-1] > ch:
                st.pop()
                k -= 1
            st.append(ch)

        while k:
            st.pop()
            k -= 1

        ans = ''.join(st).lstrip('0')
        return ans if ans else "0"
        