class Solution(object):
    def nonAdjacent(self, nums):
        n=len(nums)
        prev=nums[0]
        prev2=0
        for i in range(1,n):
            take=nums[i]
            if i>1:
                take+=prev2
            nottake=0+prev
            curri=max(take,nottake)
            prev2=prev
            prev=curri
        return prev    
    def rob(self, nums):
        n=len(nums)
        if n==1 or n==0:
            return nums[0]
        temp1 = nums[1:]
        # arr2 excludes last house
        temp2 = nums[:-1]
        return max(self.nonAdjacent(temp1),self.nonAdjacent(temp2))         
        