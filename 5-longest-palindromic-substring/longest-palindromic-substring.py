class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:return s[0]
 
        maxlen=0
        maxstr=''
        for i in range(1,len(s)):
            l,r=i-1,i
            currlen=0
            curr=''
            while l>=0 and r<len(s) and s[l]==s[r]:
                currlen+=2
                curr=s[l]+curr+s[r]
                l-=1
                r+=1
            if currlen>maxlen:
                maxlen=currlen
                maxstr=curr
        if len(s)>2:  
            for i in range(2,len(s)):
                l,r=i-2,i
                currlen=1
                curr=s[i-1]

                while l>=0 and r<len(s) and s[l]==s[r]:
                    # print('j')
                    currlen+=2
                    curr=s[l]+curr+s[r]
                    # print(curr)
                    l-=1
                    r+=1
                if currlen>maxlen:
                    maxlen=currlen
                    maxstr=curr
        if maxlen<2:return s[0]
        return maxstr
        
        


        