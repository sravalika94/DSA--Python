class Solution(object):
    def func(self,m,n):
        prev=[0]*n
        for i in range(m):
            temp=[0]*n
            for j in range(n):
                if i==0 and j==0:
                  temp[j]=1
                  continue
                if i>0:
                  up=prev[j]
                else:
                    up=0
                if j>0:
                    left=temp[j-1]
                else:
                    left=0
                temp[j]=up+left
            prev=temp
        return prev[-1]                  

    def uniquePaths(self, m, n):
        return self.func(m,n)
      
        