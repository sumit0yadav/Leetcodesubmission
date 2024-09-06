from collections import deque
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        def h(day):
            grid=[]
            dx=[0,1,0,-1]
            dy=[-1,0,1,0]
            vis=[]

            for i in range(row):
                l=[]
                ll=[]
                for j in range(col):
                    l.append(0)
                    ll.append(False)
                grid.append(l)
                vis.append(ll)


            for i in range(day):
                r,c=cells[i]
                grid[r-1][c-1]=1
                vis[r-1][c-1]=True
            q=deque()
            for i in range(col):
                if grid[0][i]==0:
                    q.append([0,i])
                    vis[0][i]=True
            # if day==1 or day ==2:print(q,day)
            while q:
                r,c=q.popleft()
                # vis[r][c]=True
                if r==row-1:
                    return True
                for i in range(4):
                    x=r+dx[i]
                    y=c+dy[i]
                    if 0<=x<row and 0<=y<col and not vis[x][y]:
                        q.append([x,y])
                        vis[x][y]=True
            return False
        ans=0
        l,r=1,len(cells)

        while l<=r:
            mid=l+(r-l)//2
            if h(mid):
                ans=mid
                l=mid+1
            else:
                r=mid-1
        # print(h(1))
        # print(h(2))
        return ans



                
        