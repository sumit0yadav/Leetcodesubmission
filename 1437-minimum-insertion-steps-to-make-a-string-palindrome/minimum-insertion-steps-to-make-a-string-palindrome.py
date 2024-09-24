from functools import lru_cache
class Solution:
    def minInsertions(self, s: str) -> int:

        def pal(s):
            if s==s[::-1]:
                return True
            return False
        if pal(s):return 0
        if len(s)<2: return 0
        @lru_cache(None)
        def h(i,j,s):
            if i>j:return 0
            if i==j:
                if s[i]!=s[j]:
                    return 1
                else:
                    return 0
            


            if s[i]==s[j]:
                return h(i+1,j-1,s)
            else:
                return 1+min(h(i+1,j,s),h(i,j-1,s))
        return h(0,len(s)-1,s)
        