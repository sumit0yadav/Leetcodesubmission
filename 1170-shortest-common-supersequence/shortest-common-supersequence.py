class Solution:
    def shortestCommonSupersequence(self, text1: str, text2: str) -> str:
        def h(i,j,t1,t2,dp,st):
            if i<0 or j<0:return 0,''
            if (i,j) in dp:
                return dp[(i,j)]
            if t1[i]==t2[j]:
                
                l,st=h(i-1,j-1,t1,t2,dp,st)
                l=l+1
                st=st+t1[i]
                
                
            else:
                l1,s1=h(i-1,j,t1,t2,dp,st)
                l2,s2=h(i,j-1,t1,t2,dp,st)

                if l1>l2:
                    l=l1
                    st=s1
                else:
                    l=l2
                    st=s2

            dp[(i,j)]=(l,st)
            return (l,st)
        dp={}
        n1=len(text1)-1
        n2=len(text2)-1
        st=''
        _,lcs= h(n1,n2,text1,text2,dp,st)

        res, i, j = "", 0, 0
        for c in lcs:
            while text1[i] != c:
                res += text1[i]
                i += 1
            while text2[j] != c:
                res += text2[j]
                j += 1
            res += c
            i, j = i + 1, j + 1
        return res + text1[i:] + text2[j:]