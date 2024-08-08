from typing import List

class Solution:
    def __init__(self):
        self.t = None
        self.n = 0

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.n = len(s)
        self.t = [None] * self.n
        return self.solve(s, 0, wordDict)

    def solve(self, s: str, idx: int, wordDict: List[str]) -> bool:
        if idx == self.n:
            return True
        
        if self.t[idx] is not None:
            return self.t[idx]
        
        for endIdx in range(idx + 1, self.n + 1):
            split = s[idx:endIdx]
            
            if split in wordDict and self.solve(s, endIdx, wordDict):
                self.t[idx] = True
                return True
        
        self.t[idx] = False
        return False

# # Example usage:
# solution = Solution()
# print(solution.wordBreak("leetcode", ["leet", "code"]))  # Output: True
# print(solution.wordBreak("applepenapple", ["apple", "pen"]))  # Output: True
# print(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # Output: False
