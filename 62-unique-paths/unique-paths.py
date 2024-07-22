class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def h(m,n,i,j,dp):
            if(i>=m or j>=n):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            if(i==m-1 and j==n-1):
                return 1
            dp[(i,j)]=h(m,n,i+1,j,dp)+h(m,n,i,j+1,dp)
            return dp[(i,j)]
        i,j=0,0
        dp={}
        return h(m,n,i,j,dp)
            
        