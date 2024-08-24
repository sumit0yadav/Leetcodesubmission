class Solution:
    def nearestPalindromic(self, s: str) -> str:
        def p10(n):
            if n < 1:
                return False
            while n % 10 == 0:
                n /= 10
            return n == 1

        if s=='11':return '9'
        if int(s)<11:return str(int(s)-1)
        if s=='100' or s=='101':return '99'
        if s=='99':return '101'
        if p10(int(s)):
            return str(int(s)-1)
        if int(s)%10==1:
            if p10(int(s)-1):
                return str(int(s)-2)




        if len(s)%2==0:
            k=len(s)//2
        else:
            k=len(s)//2+1
        pre=s[:k]
        # print(pre)
        pre1=str(int(pre)-1)
        pre3=str(int(pre)+1)
        def rev(pre):
            x=pre[::-1]
            if len(s)%2==1:

                return x[1:]
            else:
                return x

        s2=pre+rev(pre)
        # print(rev(pre))
        s1=pre1+rev(pre1)
        if len(pre3)!=len(pre):
            s3=pre3+rev(pre3)[1:]
            # print(rev(pre3))
        else:
            s3=pre3+rev(pre3)
        # print(s1)
        min1=abs(int(s1)-int(s))
        min2=abs(int(s2)-int(s))
        if min2==0:
            min2=1e9
        min3=abs(int(s3)-int(s))
        mini=min(min1,min2,min3)
        if min1==mini:
            return s1
        elif min2==mini:
            return s2
        else:
            return s3