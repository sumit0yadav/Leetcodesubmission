class Solution:
    def merge(self, l: List[List[int]]) -> List[List[int]]:
        ans=[]
        l.sort()
        curr=l[0]
        for start,end in l[1:]:
            if start<=curr[1]:
                curr[1]=max(curr[1],end)
            else:
                ans.append(curr)
                curr=[start,end]
        ans.append(curr)
        return ans
                
        