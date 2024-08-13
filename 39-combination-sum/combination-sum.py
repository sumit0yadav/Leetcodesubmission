class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # def combinationSum(candidates, target):
        def backtrack(start, current_combination, remaining_target):
            if remaining_target == 0:
                result.append(list(current_combination))
                return
            if remaining_target < 0:
                return

            for i in range(start, len(candidates)):
                # Take the current candidate
                current_combination.append(candidates[i])
                # Recursively explore with the current candidate included
                backtrack(i, current_combination, remaining_target - candidates[i])
                # Backtrack, removing the last candidate added
                current_combination.pop()

        result = []
        backtrack(0, [], target)
        return result

# # Test cases
# print(combinationSum([2, 3, 6, 7], 7))  # Output: [[2, 2, 3], [7]]
# print(combinationSum([2, 3, 5], 8))     # Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
# print(combinationSum([2], 1))           # Output: []
