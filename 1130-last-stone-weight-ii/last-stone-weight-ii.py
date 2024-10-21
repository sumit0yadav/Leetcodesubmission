class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total=sum(stones)
        target=total/2
        @cache
        def h(ind,curr):
            if curr>=target or ind==len(stones):
                return abs(total-2*curr)
            return min(h(ind+1,curr),h(ind+1,curr+stones[ind]))
        
        return h(0,0)
        