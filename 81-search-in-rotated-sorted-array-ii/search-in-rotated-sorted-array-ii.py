class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        # # def search(self, nums: List[int], target: int) -> int:
        # n=len(nums)-1
    

        # l,r=0,n
        # while l<=r:
        #     mid=l+(r-l)//2
        #     midval=nums[mid]
        #     lval=nums[l]
        #     rval=nums[r]
        #     if midval==target:
        #         return True
        #     if lval<=target<midval:
        #         r=mid-1
        #     elif lval<=midval:
        #         l=mid+1
        #     elif midval<target<=rval:
        #         l=mid+1
        #     else:
        #         r=mid-1
        # return False 
        return True if target in nums else False