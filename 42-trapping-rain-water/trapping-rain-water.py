class Solution:
    def trap(self, height: List[int]) -> int:
        # height = [4,2,0,3,2,5]
        if len(height)<3:return 0
        n=len(height)
        leftmax=[]
        rightmax=[]
        x,y=0,0
        for i in range(len(height)):
            x=max(x,height[i])
            leftmax.append(x)
            y=max(y,height[n-1-i])
            rightmax.append(y)
        rightmax=rightmax[::-1]
        # print(height)
        # print(leftmax)
        ans=0
        for i in range(len(height)):
            x=min(leftmax[i],rightmax[i])-height[i]
            ans+=max(0,x)
        # print(ans)


        # print(rightmax)
        return ans