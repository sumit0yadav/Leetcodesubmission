class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def h(i,j,t1,t2,dp):
            if i<0 or j<0:return 0
            if (i,j) in dp:
                return dp[(i,j)]
            if t1[i]==t2[j]:
                ans= 1+h(i-1,j-1,t1,t2,dp)
            else:
                ans= max(h(i-1,j,t1,t2,dp),h(i,j-1,t1,t2,dp))
            
            dp[(i,j)]=ans
            return ans

        dp={}
        n1=len(text1)-1
        n2=len(text2)-1
        return h(n1,n2,text1,text2,dp)