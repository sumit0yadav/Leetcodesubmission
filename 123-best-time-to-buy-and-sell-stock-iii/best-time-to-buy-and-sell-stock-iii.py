class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        def h(p,trans,state,ind,dp):
            if ind==len(prices) or trans==0:
                return 0
            if (trans,state,ind) in dp:
                return dp[(trans,state,ind)]
            if state=='buy':
                c1=h(p,trans,'sell',ind+1,dp)-p[ind]
                c2=h(p,trans,state,ind+1,dp)


            else:
                c1=h(p,trans-1,'buy',ind+1,dp)+p[ind]
                c2=h(p,trans,state,ind+1,dp)
            
            dp[(trans,state,ind)]=max(0,c1,c2)
            return max(0,c1,c2)
        dp={}
        return h(prices,2,'buy',0,dp)




        