from collections import deque
class Solution:
    def ladderLength(self, begin: str, end: str, wordList: List[str]) -> int:
        def change(s, i, ch):
            # ch=chr(ch)
            slist = list(s)
            slist[i] = ch
            return ''.join(slist)
        

        q=deque()
        q.append((begin,1))
        st=set(wordList)
        if end not in st:
            return 0
        while q:
            word,step=q.popleft()
            if word==end:
                return step
            for i in range(len(word)):
                original=word[i]
                for ch in range(ord('a'),ord('z')+1):
                    
                    word=change(word,i,chr(ch))
                    if word in st:
                        st.remove(word)
                        q.append((word,step+1))
                word=change(word,i,original)
        
        return 0



        