from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge the two arrays into a single list
        combined = nums1 + nums2
        combined.sort()

        def upper(arr, x):
            n = len(arr)
            low, high = 0, n - 1
            ans = n
            
            while low <= high:
                mid = low + (high - low) // 2
                if x < arr[mid]:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans
        
        def countsmallequal(arr, x):
            return upper(arr, x)
        
        low, high = combined[0],combined[len(combined)-1]
        total_len = len(combined)
        req = (total_len + 1) // 2
        
        while low <= high:
            mid = (low + high) // 2
            smallequal = countsmallequal(combined, mid)
            if smallequal < req:
                low = mid + 1
            else:
                high = mid - 1
        
        # After binary search, 'low' is the correct median value
        if total_len % 2 == 0:
            return (combined[req - 1] + combined[req]) / 2.0
        else:
            return combined[req - 1]

# Example usage:
# solution = Solution()
# print(solution.findMedianSortedArrays([1, 3], [2]))  # Output: 2.0
# print(solution.findMedianSortedArrays([1, 2], [3, 4]))  # Output: 2.5
