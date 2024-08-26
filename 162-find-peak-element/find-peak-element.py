class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        if len(nums)==2:
            if nums[0]>nums[1]:
                return 0
            else:return 1
        if nums[0]>nums[1]:return 0
        if nums[-2]<nums[-1]:return len(nums)-1
        l,r=0,len(nums)-1

        while l<r:
            if abs(l-r)==1:
                if nums[l]>nums[r]:return l
                else:return r
            mid=l+(r-l)//2
            if nums[mid-1]<nums[mid] and nums[mid+1]<nums[mid]:
                return mid
            if mid==len(nums)-1 and nums[mid-1]<nums[mid]:
                return mid
            if mid==0 and nums[mid]>nums[mid+1]:
                return mid
            if nums[mid-1]<nums[mid]<nums[mid+1]:
                l=mid+1
            elif nums[mid-1]>nums[mid]>nums[mid+1]:
                r=mid-1
            else:
                l=l-1
                r=r-1
        return l
            



        