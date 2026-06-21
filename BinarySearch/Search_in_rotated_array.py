class Solution(object):
    def search(self, nums,k):
        n=len(nums)
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==k:
                return True
            if nums[low]==nums[mid] and nums[mid]==nums[high]:
                low=low+1
                high=high-1
                continue  
            if nums[low]<=nums[mid]:
                if nums[low]<=k and k<=nums[mid]:
                  high=mid-1
                else:
                  low=mid+1
            else:          
                if nums[mid]<=k and k<=nums[high]:  
                  low=mid+1
                else:
                    high=mid-1
            
        return False
        