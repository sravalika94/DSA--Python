class Solution(object):
    def reverse(self,arr,start,end):
        while start<end:
          arr[start],arr[end]=arr[end],arr[start]
          start += 1
          end -= 1

    def rotate(self, arr, k):
        n=len(arr)
        k= k%n
        self.reverse(arr,0,n-1)
        self.reverse(arr,0,k-1)
        self.reverse(arr,k,n-1)
        return arr