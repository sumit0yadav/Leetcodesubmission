class Solution:
    def addBinary(self, s1: str, s2: str) -> str:
        # s1='111'
        # s2='11'
        c=0
        i,j=len(s1)-1,len(s2)-1
        ans=''
        while i>-1 and j>-1:
            ii=s1[i]
            jj=s2[j]

            s=int(ii)+int(jj)+c
            if s==0 or s==1:
                ans=ans+str(s)
                c=0
            elif s==2:
                ans=ans+str(0)
                c=1
            elif s==3:
                ans+=str(1)
                c=1
            i-=1
            j-=1

        # print(i,j,ans)
        while i>-1:
            ii=s1[i]
            

            s=int(ii)+c
            if s==0 or s==1:
                ans=ans+str(s)
                c=0
            elif s==2:
                ans=ans+str(0)
                c=1
            elif s==3:
                ans+=str(1)
                c=1
            i-=1
        # print(ans)
        while j>-1:
            # ii=s1[i]
            jj=s2[j]

            s=int(jj)+c
            if s==0 or s==1:
                ans=ans+str(s)
                c=0
            elif s==2:
                ans=ans+str(0)
                c=1
            elif s==3:
                ans+=str(1)
                c=1
            
            j-=1
        if c==1:
            ans=ans+str(c)

        ans=ans[::-1]
        return ans


        