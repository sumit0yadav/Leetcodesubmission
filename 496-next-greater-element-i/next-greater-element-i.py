class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ind1={}
        ind2={}
        for i in range(len(nums1)):
            ind1[nums1[i]]=i
        for j in range(len(nums2)):
            ind2[nums2[j]]=j
        
        ans=[-1]*len(nums1)
        for i in range(len(nums1)):
            if i==1:
                print(nums1[i])
            ind=ind2[nums1[i]]
            if i==1:print(ind)
       
            for k in range(ind+1,len(nums2)):
             
                if nums2[k]>nums1[i]:
                    
                    ans[i]=nums2[k]
                    break
            
        return ans


        