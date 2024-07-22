class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def h(grid,dp,m,n,i,j):
            if(i>=m or j>=n):
                return 0
            if(grid[i][j]==1):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            if i==m-1 and j==n-1:
                return 1
            dp[(i,j)]=h(grid,dp,m,n,i+1,j)+h(grid,dp,m,n,i,j+1)
            return dp[(i,j)]
        dp={}
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        return h(obstacleGrid,dp,m,n,0,0)



        