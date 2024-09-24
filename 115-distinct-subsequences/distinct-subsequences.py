from functools import lru_cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s)<len(t):return 0
        @lru_cache(None)
        def h(s,t,i,j):
            

            if j==len(t):
                return 1
            if i>=len(s):
                return 0
            if s[i]==t[j]:
                take=h(s,t,i+1,j+1)
                nottake=h(s,t,i+1,j)
                return take+nottake

            else:
                return h(s,t,i+1,j)


            
        return h(s,t,0,0)
        
