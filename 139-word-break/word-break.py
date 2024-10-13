class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset=set(wordDict)
        @cache
        def h(ind):
            # if ind>=len(s):return False
            if ind==len(s):return True
            for i in range(ind+1,len(s)+1):
                tmp=s[ind:i]
                if tmp in wordset:
                    
                    if h(i):
                        return True
            return False
        return h(0)
        