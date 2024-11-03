class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def count(i,k,prev,cnt):
            if k<0:return 1e9
            if i==len(s): return 0
            if s[i]==prev:
                incr= 1 if cnt in [1,9,99,999] else 0
                res=incr+count(i+1,k,prev,cnt+1)
            else:
                res=min(
                    count(i+1,k-1,prev,cnt),
                    1+count(i+1,k,s[i],1)
                )
            return res
        return count(0,k,"",0)
        