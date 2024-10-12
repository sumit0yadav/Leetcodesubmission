class Solution:
    def hIndex(self, cit: List[int]) -> int:
        ans=[0]*(len(cit)+1)
        for ind in cit:
            if ind>=len(cit):
                ans[-1]+=1
            else:
                ans[ind]+=1
        res=0
        cnt=0
        print(ans)
        for i in range(len(ans)-1,-1,-1):
            cnt+=ans[i]
            if i<=cnt:return i
        return -1

        