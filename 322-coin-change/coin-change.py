class Solution:
    def coinChange(self, l: List[int], amt: int) -> int:
        l.sort()
        @cache
        def h(ind,s):
            if ind<0:return 1e9
            if s<0:return 1e9
            if s==0:return 0
            take,nottake=1e9,1e9
            if s>=l[ind]:
                take=1+h(ind,s-l[ind])
            nottake=h(ind-1,s)
            ans=min(take,nottake)
            return ans
        x= h(len(l)-1,amt)
        if x==1e9:return -1
        return x
            



        