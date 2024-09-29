class Solution:
    def shortestCommonSupersequence(self, t1: str, t2: str) -> str:

        def h(i,j,t1,t2,dp):
            if i<0 or j<0:
                return 0,''
            
            if (i,j) in dp:
                return dp[(i,j)]

            if t1[i]==t2[j]:
                l,s= h(i-1,j-1,t1,t2,dp)
                l=l+1
                s=s+t1[i]
            else:

                l1,s1=h(i-1,j,t1,t2,dp)
                l2,s2=h(i,j-1,t1,t2,dp)

                if l1>l2:
                    
                    
                    l=l1
                    s=s1
                else:
                    l=l2
                   
                    s=s2
                
                
            dp[(i,j)]=(l,s)
            return l,s

        n1,n2=len(t1)-1,len(t2)-1
        dp={}
        _,lcs=h(n1,n2,t1,t2,dp)

        res,i,j='',0,0
        for char in lcs:
            while t1[i]!=char:
                res+=t1[i]
                i+=1
            while t2[j]!=char:
                res+=t2[j]
                j+=1
            res+=char
            i+=1
            j+=1
        ans=res+t1[i:]+t2[j:]
        return ans
            



        