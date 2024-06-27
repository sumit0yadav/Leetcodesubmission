class Solution:
    def trailingZeroes(self, n: int) -> int:
        import math
        
        cnt=0
        while(n>0):
            cnt+=math.floor(n//5)
            n=n//5
        return cnt
        