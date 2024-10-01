class Solution:
    from collections import deque
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def h(mid):
            grid=[]
            vis=[]
            for i in range(row):
                l=[]
                ll=[]
                for j in range(col):
                    l.append(0)
                    ll.append(False)
                grid.append(l)
                vis.append(ll)
            for i in range(mid):
                x,y=cells[i]
                vis[x-1][y-1]=True
                grid[x-1][y-1]=1
            q=deque()
            for i in range(col):
                if vis[0][i]==False:
                    q.append((0,i))
            dx=[-1,1,0,0]
            dy=[0,0,1,-1]
            while q:
                x,y=q.popleft()
                if vis[x][y]:continue
                
                if x==row-1:return True
                vis[x][y]=True
                
                
                for i in range(4):
                    xx=x+dx[i]
                    yy=y+dy[i]
                    if 0<=xx<row and 0<=yy<col and not vis[xx][yy]:
                        q.append((xx,yy))
            return False   

        l,r=1,len(cells)
        ans=0
        while l<=r:
            mid=l+(r-l)//2
            if h(mid):
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans
        