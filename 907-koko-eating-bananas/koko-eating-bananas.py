class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        if len(piles)==1:
            return max(1,math.ceil(piles[0]/h))
        


        def checktime(pile,k):
            time=0
            piles=pile.copy()
            for i in range(len(piles)):
                time=time+piles[i]//k
                if piles[i]%k!=0:
                    time+=1
            return time

        l,r=1,max(piles)
        ans=-1
        while l<=r:
            # print('s')
            mid=l+(r-l)//2
            
            
            times=checktime(piles,mid)
            
            
            if times<=h:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans



        