from collections import deque
class Solution:
    def ladderLength(self, bw: str, ew: str, wl: List[str]) -> int:

        def change(word,ind,ch):
            l=list(word)
            l[ind]=ch
            return ''.join(l)
        if ew not in wl: 
            return 0
        q= deque()
        step=1
        q.append([bw,step])
        ws=set(wl)
        if bw in ws:ws.remove(bw)
        while q:
            curr,step=q.popleft()
            if curr==ew:return step
            for i in range(len(curr)):
                char=curr[i]
                for ch in range(ord('a'),ord('z')+1):
                    new=change(curr,i,chr(ch))
                    if new in ws:
                        ws.remove(new)
                        q.append([new,step+1])
                curr=change(curr,i,char)
        return 0

            
        