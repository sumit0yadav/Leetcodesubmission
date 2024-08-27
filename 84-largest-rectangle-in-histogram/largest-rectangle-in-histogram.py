class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        if len(h)==0 :
            return 0
        if len(h)==1:
            return len(h)*min(h)
        if len(h)==2:
            # if 0 in h:
            #     if h[0]==0:return h[1]
            #     else:return h[0]
            return max(len(h)*min(h),max(h))
            
        lessfromleft=[None]*len(h)
        lessfromright=[None]*len(h)
        lessfromleft[0]=-1
        lessfromright[-1]=len(h)
        for i in range(1,len(h)):
            p=i-1
            while p>=0 and h[p]>=h[i]:
                p=lessfromleft[p]
            lessfromleft[i]=p
        for i in range(len(h)-2,-1,-1):
            p=i+1
            while p<len(h) and h[p]>=h[i]:
                p=lessfromright[p]
            lessfromright[i]=p
        ans=0
        for i in range(len(h)):
            ans=max(ans,h[i]*(lessfromright[i]-lessfromleft[i]-1))
        return ans

        

        