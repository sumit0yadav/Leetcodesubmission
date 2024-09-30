class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k==1:return nums
        if k>=len(nums):return [max(nums)]

        stack=[]
        maxval=-1e9
        maxind=-1
        ans=[]
        for i in range(len(nums)):

            if stack and maxind+k<=i:
                x,y=stack.pop(0)
                maxind=stack[0][1]
                maxval=stack[0][0]

            if maxval<=nums[i]:
                maxind=i
                maxval=nums[i]
                stack=[]
                stack.append([maxval,maxind])
            else:
                while stack and nums[i]>=stack[-1][0]:
                    stack.pop()
                stack.append([nums[i],i])
                
            # print(stack)
            if stack and i>=k-1:
                ans.append(stack[0][0])
        return ans


        