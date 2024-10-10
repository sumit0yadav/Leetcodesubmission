class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        num=[x for x in range(1,n+1)]

        def h(ind,res):
            if len(res)==k:
                ans.append(list(res))
                return
            if ind>=len(num):return
            res.append(num[ind])
            take=h(ind+1,res)
            res.pop()
            nottake=h(ind+1,res)
        h(0,[])
        return ans

        