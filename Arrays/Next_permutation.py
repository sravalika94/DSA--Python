class Solution(object):
    def nextPermutation(self, nums):
       n=len(nums)
       index=-1
       for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                index=i
                break
       if index==-1: 
         nums.reverse()
         return
       for i in range(n-1,index,-1):
            if nums[i]>nums[index]:
                nums[index],nums[i]=nums[i],nums[index]
                break
       nums[index+1:]=reversed(nums[index+1:]) 