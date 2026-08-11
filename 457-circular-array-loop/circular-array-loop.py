class Solution(object):
    def circularArrayLoop(self, nums):
        n = len(nums)

        def nxt(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            direction = nums[i] > 0
            slow = fast = i

            while True:
                ns = nxt(slow)
                nf = nxt(fast)

                if nums[ns] == 0 or (nums[ns] > 0) != direction:
                    break

                if nums[nf] == 0 or (nums[nf] > 0) != direction:
                    break
                nf = nxt(nf)
                if nums[nf] == 0 or (nums[nf] > 0) != direction:
                    break

                slow = ns
                fast = nf

                if slow == fast:
                    if slow == nxt(slow):   # one-element loop
                        break
                    return True

            j = i
            while nums[j] != 0 and (nums[j] > 0) == direction:
                nxtj = nxt(j)
                nums[j] = 0
                j = nxtj

        return False