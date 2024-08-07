class Solution:
    def myAtoi(self, s: str) -> int:
        # s2=s.replace(" ","")
        l=[]
        # print(ord(l[0]),l)
        l2=[]
        i=0
        while i<len(s) and s[i]==' ':
            
            i+=1
        while i<len(s):
            l.append(s[i])
            i+=1

        i=0
        while i<len(l):
            if i==0 and ord(l[i])==45:
                l2.append(l[i])
                i+=1
            if i==0 and l[i]=='+':
                # l2.append(l[i])
                i+=1
            
            
            while i<len(l) and (48<=ord(l[i])<=57):
                l2.append(l[i])
                i+=1
            break
        ans=''.join(l2)
        if len(l2)==0:return 0
        if len(l2)==1 and l2[0]=='-':return 0
        aa=int(ans)
        # print(aa,type(aa))
        if aa<-2**31:return -2**31
        if aa>2**31-1: return 2**31-1
        return aa
        