class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def pal(s):
            return s==s[::-1]
        
        def h(s,i,j,res,ans):

            if i==j:
                res.append(list(ans))
                return
            if i>j:
                return
            


            for k in range(i,j):
                if pal(s[i:k+1]):
                    ans.append(s[i:k+1])
                    h(s,k+1,j,res,ans)
                    ans.pop()
                else:
                    continue
        res=[]
        h(s,0,len(s),res,[])
        return res

                    

        