class Solution:
    def preprocess_palindrome(self, s: str):
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        # All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True

        # Check for substrings of length 2
        for i in range(n - 1):
            dp[i][i + 1] = (s[i] == s[i + 1])

        # Check for substrings of length 3 or more
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])

        return dp

    def is_palindrome(self, dp, i, j):
        return dp[i][j]

    def minCut(self, s: str) -> int:
        if s == s[::-1]:  # If the whole string is already a palindrome, no cuts are needed
            return 0
        
        n = len(s)
        dp_palindrome = self.preprocess_palindrome(s)  # Preprocess palindromes

        def h(s, i, j, dp):
            if i >= j:  # Base case: No cuts needed
                return 0
            
            # If the substring s[i:j+1] is already a palindrome, no cuts are needed
            if self.is_palindrome(dp_palindrome, i, j):
                return 0
            
            if (i, j) in dp:  # Memoization lookup
                return dp[(i, j)]
            
            mincut = float('inf')  # Initialize with a large number

            # Try all possible cuts
            for k in range(i, j):
                if self.is_palindrome(dp_palindrome, i, k):  # Only recurse if s[i:k+1] is a palindrome
                    ans = 1 + h(s, k + 1, j, dp)  # 1 cut between s[i:k] and s[k+1:j]
                    mincut = min(ans, mincut)

            dp[(i, j)] = mincut  # Memoize the result
            return mincut

        dp = {}
        return h(s, 0, n - 1, dp)  # Start the recursion for the full string
