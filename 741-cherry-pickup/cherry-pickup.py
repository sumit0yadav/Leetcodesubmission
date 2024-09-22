
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n=len(grid)
        
        # @lru_cache(None)
        def h(grid,n,r1,c1,r2,c2,dp):
            if r1>=n or r2>=n or c1>=n or c2>=n or grid[r1][c1]==-1 or grid[r2][c2]==-1:
                return -1e9
            if (r1==n-1 and c1==n-1):return grid[r1][c1]
            if (r2==n-1 and c2==n-1):return grid[r2][c2]
            ch=0
            if (r1,r2,c1,c2) in dp:
                return dp[(r1,r2,c1,c2)]
            if r1==r2 and c1==c2:
                ch=grid[r1][c1]
            else:
                ch=grid[r1][c1]+grid[r2][c2]
            a=h(grid,n,r1+1,c1,r2+1,c2,dp)
            b=h(grid,n,r1+1,c1,r2,c2+1,dp)
            c=h(grid,n,r1,c1+1,r2+1,c2,dp)
            d=h(grid,n,r1,c1+1,r2,c2+1,dp)
            dp[(r1,r2,c1,c2)]=max(a,b,c,d)+ch
            return ch+max(a,b,c,d)
        dp={}
        return max(0,h(grid,n,0,0,0,0,dp))

            



        