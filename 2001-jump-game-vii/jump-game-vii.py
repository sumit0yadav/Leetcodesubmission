
from collections import deque
class Solution:
    def canReach(self, s: str, mini: int, maxi: int) -> bool:
        q=deque()
        q.append(0)
        for i in range(1,len(s)):
            if s[i]=='0':

                while q and q[0]<i-maxi:
                    q.popleft()
                if not q:return False
                prev=q[0]
                if prev+mini<=i<=prev+maxi:
                    q.append(i)
                    if i==len(s)-1:
                        return True

        return False



        