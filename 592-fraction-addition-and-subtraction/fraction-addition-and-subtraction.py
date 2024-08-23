class Solution:
    def fractionAddition(self, exp: str) -> str:
        def gcdf(a,b):
            import math
            return math.gcd(a,b)
        if '/' not in exp:
            return exp

        # ints = list(map(int, re.findall('[+-]?\d+', exp)))
        # print(ints)

        l=[]
        i=0
        sign='+'
        while i<len(exp):
            if exp[i]=='/':
                i+=1
                sign='+'
            elif exp[i]=='-':
                sign='-'
                
                i+=1
            elif exp[i]=='+':
                sign='+'
                
                i+=1

            st=''
            while i<len(exp) and 48<=ord(exp[i])<=57:
                st+=exp[i]
                i+=1
            num=int(st)
            if sign=='-':
                num=-num
            l.append(num)
        # print(l)
        den,num=1,0
        for i in range(0,len(l),2):
            n1=l[i]
            d1=l[i+1]
            num=d1*num+n1*den
            den=den*d1
            # print(num,den)
        gcd=gcdf(num,den)
        num=int(num)//gcd
        den=int(den)//gcd

        return str(num)+'/'+str(den)







    


        