class Solution:
    def maxArea(self, h: List[int]) -> int:
        l,r=0,len(h)-1
        maxi=-1e9
        while l<=r:
            area=(r-l)*min(h[l],h[r])
            maxi=max(maxi,area)
            if h[l]<h[r]:
                l+=1
            else:
                r-=1
        return maxi
        