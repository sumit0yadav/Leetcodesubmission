class Solution:
    def maxProduct(self, l: List[int]) -> int:

        if len(l)==1:
            return l[0]
        res1=1
        ans1=-1e9
        res2=1
        ans2=-1e9
        for i in range(len(l)):
            if l[i]==0:
                res1=1
            elif l[i]!=0:
                res1=res1*l[i]
                ans1=max(res1,ans1)
            if l[len(l)-1-i]==0:
                res2=1
            elif l[len(l)-1-i]!=0:
            
                res2=res2*l[len(l)-1-i]
                ans2=max(ans2,res2)
        return max(0,ans1,ans2)
        
        