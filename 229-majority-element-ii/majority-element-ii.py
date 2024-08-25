# class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:
#         if not nums or len(nums)==1:
#             return nums
#         cnt,cand=0,-1

#         for n in nums:
#             if cand==n:
#                 cnt+=1
#             elif cnt==0:
#                 cand=n
#                 cnt+=1
#             elif cand!=n:
#                 cnt-=1
            
#         cand1=cand
#         cand=-1
#         cnt=0
#         for n in nums:
#             if n==cand1:
#                 continue
#             else:
                
#                 if cand==n:
#                     cnt+=1
#                 elif cnt==0:
#                     cand=n
#                     cnt+=1
#                 elif cand!=n:
#                     cnt-=1
#         cand2=cand
#         print(cand1,cand2)
#         l=[]
#         return [n for n in (cand1,cand2) if nums.count(n)>len(nums)//3]

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        # Phase 1: Find potential candidates
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # Phase 2: Validate the candidates
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        # Collect valid candidates
        result = []
        if count1 > len(nums) // 3:
            result.append(candidate1)
        if count2 > len(nums) // 3:
            result.append(candidate2)

        return result


        