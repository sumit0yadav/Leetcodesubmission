from typing import List

class Solution:
    # from typing import List

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        t = [None] * n  # Memoization array
        
        def solve(idx: int) -> bool:
            if idx == n:
                return True
            
            if t[idx] is not None:
                return t[idx]
            
            for endIdx in range(idx + 1, n + 1):
                split = s[idx:endIdx]
                
                if split in wordDict and solve(endIdx):
                    t[idx] = True
                    return True
            
            t[idx] = False
            return False
        
        return solve(0)

    # # Example usage:
    # print(wordBreak("leetcode", ["leet", "code"]))  # Output: True
    # print(wordBreak("applepenapple", ["apple", "pen"]))  # Output: True
    # print(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # Output: False
