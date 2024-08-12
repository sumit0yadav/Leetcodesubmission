from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k==1:
            return nums
        if k>=len(nums):
            return [max(nums)]
        # nums = [122,1,3,4,6,3,8,9,10,12,56]


        # k = 10
        q=deque()
        ans=[]
        
        maxv=-1e9
        maxind=-1
        # for i in range(k):
            
        #     if(i>maxind):
        #         q.append((nums[i],i))
        #     if maxv<nums[i]:
               
        #         q=deque()
        #         maxv=nums[i]
        #         maxind=i
                
        #         q.append((nums[i],i))
      
       
        # ans.append(q[0][0])
        for i in range(len(nums)):
        
         
            if i-maxind>=k:
                
                a,b=q.popleft()
                maxv=q[0][0]
                maxind=q[0][1]

            if nums[i]>=maxv:
                # if i==5:print('b')
                
                q=deque()
                maxv=nums[i]
                maxind=i
                q.append((nums[i],i))
            else:
               
           
                while q and nums[i]>=q[-1][0]:
                    x,y=q.pop()
                
                if ( q and q[-1][0]>nums[i]):
                    q.append((nums[i],i))
                if not q:
                    q.append((nums[i],i))
                    maxv=nums[i]
                    maxind=i
            if i>=k-1:
                ans.append(q[0][0])
            # print(q,nums[i])
        print(ans)
        return ans


# print(stack,maxind)
        