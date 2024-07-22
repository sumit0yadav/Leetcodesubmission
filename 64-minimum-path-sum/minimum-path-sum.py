class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        def h(g,m,n,i,j,dp):
            if (i>=m or j>=n):
                return float('inf')
            if i==m-1 and j==n-1:
                return g[i][j]
            if (i,j) in dp:
                return dp[(i,j)]
            left,right=float('inf'),float('inf')
            left=g[i][j]+h(g,m,n,i+1,j,dp)
            right=g[i][j]+h(g,m,n,i,j+1,dp)
            dp[(i,j)]=min(left,right)
            return dp[(i,j)]
        dp={}
        return h(grid,len(grid),len(grid[0]),0,0,dp)
        