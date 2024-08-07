class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Step 1: Calculate factorials
        factorials = [1] * (n + 1)
        for i in range(1, n + 1):
            factorials[i] = factorials[i - 1] * i
        
        # Step 2: Create a list of numbers to get the permutation from
        numbers = list(range(1, n + 1))
        
        # Adjust k to be zero-indexed
        k -= 1
        
        # Step 3: Build the k-th permutation
        result = []
        for i in range(1, n + 1):
            index = k // factorials[n - i]
            result.append(str(numbers[index]))
            numbers.pop(index)
            k %= factorials[n - i]
        
        return ''.join(result)

# # Example usage
# solution = Solution()
# print(solution.getPermutation(3, 3))  # Output: "213"
