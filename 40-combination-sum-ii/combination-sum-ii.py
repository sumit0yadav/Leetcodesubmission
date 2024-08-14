from collections import Counter
class Solution:
    def combinationSum2(self, arr: List[int], target: int) -> List[List[int]]:
        if min(arr)==max(arr):
            if arr[0]*len(arr)>target and target%arr[0]==0:
                return [[arr[0]]*(target//arr[0])]




        def hashh(curr):
            h={}
            for ele in curr:
                if ele in h:
                    h[ele]+=1
                else:
                    h[ele]=1
            return h


        def h(curr,target,start):

            if target==0:
                
                
                ans.append(list(curr))
            if target<0:
                return
            for i in range(start,len(arr)):
                if i>start and arr[i]==arr[i-1]:
                    continue
                curr.append(arr[i])
                h(curr,target-arr[i],i+1)
                curr.pop()
        ans=[]
        hs=set()
        curr=[]
        arr.sort()
        h(curr,target,0)

        return ans
        