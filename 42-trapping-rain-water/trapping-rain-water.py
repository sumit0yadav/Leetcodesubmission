class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left=[]
        right=[0]*n

        lmax=height[0]
        rmax=height[n-1]




        for i in range(0,len(height)):
            left.append(lmax)
            if(lmax<height[i]):
                
                lmax=height[i]
            right[n-i-1]=rmax
            if(rmax<height[n-i-1]):
                rmax=height[n-1-i]
        right[n-1]=0
        ans=[]
        water=0
        for i in range(len(height)):
            val=min(left[i],right[i])-height[i]
            if(val<0):
                water=water
                
            else:
                water=water+val
        return water