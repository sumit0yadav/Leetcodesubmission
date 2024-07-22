class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        def h(t,n,i,dp):
            if(n==len(t)):
                return 0
            if (i,n) in dp:
                return dp[(i,n)]

            # l,r=float('inf'),float('inf')

            l=t[n][i]+h(t,n+1,i,dp)
            r=t[n][i]+h(t,n+1,i+1,dp)

            dp[(i,n)]=min(l,r)
            return dp[(i,n)]
        dp={}
        return h(triangle,0,0,dp)
