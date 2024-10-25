from collections import Counter,defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s==t:return s
        if not s or not t or len(s)<len(t):
            return ""
        req_freq=Counter(t)
        window_freq=defaultdict(int)

        reqlen=len(req_freq)
        currlen=0
        windowlen=0
        window=""
        minilen=1e9
        minians=""
        l,r=0,0

        while r<len(s):
            char=s[r]
            window_freq[char]+=1
            if req_freq[char]==window_freq[char]:
                currlen+=1
            
            # print(window_freq)
            while l<=r and currlen==reqlen:

                if minilen>(r-l+1):
                    minilen=r-l+1
                    minians=s[l:r+1]
                char=s[l]
                window_freq[char]-=1
                if char in req_freq and req_freq[char]>window_freq[char]:
                    currlen-=1
                l+=1

            r+=1
        return minians




        
        