from collections import defaultdict
class Solution:
    def largestPalindromic(self, nums: str) -> str:

        
    # def h(nums):
        hm=defaultdict(int)
        for ele in nums:
            hm[int(ele)]+=1
        if 0 in hm:
            if hm[0]==len(nums):
                return '0'
            if hm[0]==len(nums)-1:
                del hm[0]

        
        l=[]
        for ele in hm:
            l.append([ele,hm[ele]])
        l.sort(reverse=True)

        # return l
        x=-1
        for i in range(len(l)):
            if l[i][1]%2==1:
                x=l[i][0]
                break
        l2=[]
        # print(l,x)
        if x!=-1:
            
            for i in range(len(l)):
                ele=l[i]
                if ele[1]%2==1:
                    # print('kk',ele)
                    ele[1]-=1

                    if ele[1]!=0:
                        # print('kk')
                        l2.append(ele)
                else:
                    l2.append(ele)
        else:
            l2=l
        size=0
        for i in range(len(l2)):
            size+=l2[i][1]
        size=int(size//2)
        # print(size)
        if x!=-1:
            size+=1
        # print(size)
        res=[-1]*size
        r=len(res)-1
        if x!=-1:
            res[r]=x
            r=r-1
        j=len(l2)-1
        #- -- 9
        # print(res,r,j)
        # print(l2)
        while r>-1 and j>-1:
            num=l2[j][0]
            val=l2[j][1]/2
            while val>0:
                # print(num,val,r,j)
                res[r]=num
                val=val-1
                r-=1
            j-=1
            # print(res)


        res2=[str(c) for c in res]
        # print(res2) 
        anss=''.join(res2)
        i=0
        while anss[i]=='0':
            i=i+1
        ans=anss[i:]

        if x==-1:
            a=ans+ans[::-1]
        else:
            a=ans[:-1]+ans[::-1]
        

        return a
            

        