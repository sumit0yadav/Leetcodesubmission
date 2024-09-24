class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)<3:return len(points)
        def slope(x,y):
            if y[0]-x[0]==0:return 1e9
            return (y[1]-x[1])/(y[0]-x[0])
        ans=-1e9
        val=[]
        n=len(points)
        for i in range(n-2):
            
            
            for j in range(i+1,n-1):
                res=2
                curr=[i,j]
                for k in range(j+1,n):
                    if slope(points[i],points[j])==slope(points[j],points[k]):
                        res+=1
                        curr.append(k)

                if ans<res:
                    ans=res
                    val=curr
        print(val)
        return ans

        