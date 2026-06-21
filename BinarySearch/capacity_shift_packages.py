class Solution(object):
      def needed(self,weights,cap):
        load=0
        days=1
        for weight in weights:
            if load+weight>cap:
                days=days+1
                load=weight
            else:
                load+=weight 
        return days          
      def shipWithinDays(self, weights, days):
       low=max(weights)
       high=sum(weights)
       while low<=high:
         mid=(low+high)//2
         needed=self.needed(weights,mid)
         if needed<=days:
            high=mid-1
         else:
            low=mid+1  
       return low
        