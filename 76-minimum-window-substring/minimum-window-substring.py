class Solution:
    from collections import Counter

    def minWindow(self, s: str, t: str) -> str:
        # Step 1: Base case checks
        if not s or not t or len(t) > len(s):
            return ""

        # Step 2: Count the frequency of each character in t
        required = Counter(t)  # Dict with frequency of characters in t
        window_counts = {}  # Window character counts

        # Step 3: Initialize the pointers and necessary variables
        l, r = 0, 0  # Sliding window pointers
        required_chars = len(required)  # Number of unique characters in t
        formed = 0  # Tracks how many characters meet the requirement in current window

        min_length = float("inf")  # The size of the smallest window
        min_window = ""  # The smallest window substring

        # Step 4: Start sliding the window
        while r < len(s):
            # Add current character to the window count
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1

            # If the current character count in window matches the required count, increment `formed`
            if char in required and window_counts[char] == required[char]:
                formed += 1

            # Step 5: Try to shrink the window from the left as long as it's valid
            while l <= r and formed == required_chars:
                char = s[l]

                # Check if the current window is smaller than the previously found smallest window
                window_size = r - l + 1
                if window_size < min_length:
                    min_length = window_size
                    min_window = s[l:r + 1]

                # Now shrink the window by removing the character at position `l`
                window_counts[char] -= 1
                if char in required and window_counts[char] < required[char]:
                    formed -= 1

                l += 1  # Move the left pointer forward to shrink the window

            r += 1  # Expand the window by moving the right pointer

        return min_window if min_length != float("inf") else ""
