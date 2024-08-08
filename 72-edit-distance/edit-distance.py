class Solution:
    def minDistance(self, w1: str, w2: str) -> int:

        def h(w1,w2,i,j,dp):
            if i<0 and j<0:
                return 0
            if i<0:return j+1
            if j<0:return i+1
            if (i,j) in dp:
                return dp[(i,j)]
            if w1[i]==w2[j]:
                dp[(i,j)]=h(w1,w2,i-1,j-1,dp)
                return dp[(i,j)]
            if w1[i]!=w2[j]:
                insert=1+h(w1,w2,i,j-1,dp)
                delete=1+h(w1,w2,i-1,j,dp)
                replace=1+h(w1,w2,i-1,j-1,dp)
            dp[(i,j)]= min(insert,delete,replace)
            return dp[(i,j)]
        dp={}
        return h(w1,w2,len(w1)-1,len(w2)-1,dp)
        