
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
    
        
        def h(p,i,buy,k,dp):
            if k==0 or i==len(p):return 0
            if (i,buy,k) in dp:
                return dp[(i,buy,k)]
            profit=0
            if buy==0:

                c1=h(p,i+1,1,k,dp)-p[i]
                c2=h(p,i+1,0,k,dp)
            else:
                c1=h(p,i+1,0,k-1,dp)+p[i]
                c2=h(p,i+1,1,k,dp)
            profit=max(profit,c1,c2)
            dp[(i,buy,k)]=profit
            return profit
        dp={}
        return h(prices,0,0,k,dp)


        