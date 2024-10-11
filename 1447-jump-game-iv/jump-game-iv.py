from collections import defaultdict
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr)==1:
            return 0
        
        hm=defaultdict(list)
        for i in range(len(arr)):
            hm[arr[i]].append(i)
        q=deque()
        vis=set()
        q.append(0)

        step=0
        while q:
            
            size=len(q)
            step+=1


            for i in range(size):
                curr=q.popleft()
                vis.add(curr)
                if curr==len(arr)-1:
                    return step-1
                if -1<curr-1 and curr-1 not in vis:
                    q.append(curr-1)
                if curr+1<len(arr) and curr+1 not in vis:
                    q.append(curr+1)
                for ele in hm[arr[curr]]:
                    if 0<=ele<len(arr) and ele not in vis and ele!=curr:
                        q.append(ele)
                hm[arr[curr]].clear()
        return step



        



        