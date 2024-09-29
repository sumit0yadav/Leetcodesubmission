class Solution:
    def candy(self, r: List[int]) -> int:
        if len(r)==1:return 1
        if len(r)==2:
            if r[0]==r[1]:
                return 2
            else:
                return 3
        l=[1]*len(r)
        n=len(r)
        for i in range(1,len(r)):
            if r[i-1]<r[i]:
                l[i]=l[i-1]+1
        print(l)
        for i in range(1,len(r)):
            if r[-i]<r[-i-1]:
                l[-i-1]=max(l[-1-i],l[-i]+1)
        print(l)
        return sum(l)
        
# class Solution:
#     def candy(self, nums: List[int]) -> int:

#         n=len(nums)
#         if n<=1:return n

#         l=[1]*n
#         for i in range(1,n):
#             if nums[i]>nums[i-1]:
#                 l[i]=l[i-1]+1
#         print(l)
#         for i in range(n-1,0,-1):
#             if nums[i-1]>nums[i]:
#                 l[i-1]=max(l[i]+1,l[i-1])
#         print(l)
#         return sum(l)
        