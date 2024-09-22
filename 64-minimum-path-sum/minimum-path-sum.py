class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:


        def h(grid,i,j,dp):
            if i>=len(grid) or j>=len(grid[0]):return 1e9
            if i==len(grid)-1 and j==len(grid[0])-1:
                return grid[i][j]
            if (i,j) in dp:
                return dp[(i,j)]
            right=h(grid,i+1,j,dp)
            bottom=h(grid,i,j+1,dp)

            val=min(right,bottom)+grid[i][j]
            dp[(i,j)]=val
            return val
        dp={}
        return h(grid,0,0,dp)


        