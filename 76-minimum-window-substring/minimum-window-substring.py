class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        if not s or not t or len(t)>len(s):
            return ''
        req_freq=Counter(t)
        window_freq={}

        min_length=1e9
        min_window=''
        req_char=len(req_freq)
        formed=0
        l,r=0,0
        while r<len(s):
            char=s[r]

            window_freq[char]=window_freq.get(char,0)+1
            if char in req_freq and window_freq[char]==req_freq[char]:
                formed+=1
            while l<=r and formed==req_char:
                char=s[l]
                windowsize=r-l+1
                if min_length>windowsize:
                    min_length=windowsize
                    min_window=s[l:r+1]
                window_freq[char]-=1
                if char in req_freq and window_freq[char]<req_freq[char]:
                    formed-=1
                l=l+1
            r+=1
        return min_window if min_length != float("inf") else ""


        