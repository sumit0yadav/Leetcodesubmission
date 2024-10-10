class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]

        def h(l,r,s):
            if len(s)==2*n:
                ans.append(s)
                return 
            if l<n:
                h(l+1,r,s+'(')
            if r<l:
                h(l,r+1,s+')')
        h(0,0,'')
        return ans
        
            
        