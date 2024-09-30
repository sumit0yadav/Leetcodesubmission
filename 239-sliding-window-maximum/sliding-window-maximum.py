class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        if k >= len(nums):
            return [max(nums)]

        stack = []  # Using stack instead of deque
        ans = []
        maxv = -1e9
        maxind = -1

        for i in range(len(nums)):

            # Remove the elements which are out of this window
            if i - maxind >= k:
                stack.pop(0)  # Remove the first element since it's out of the window
                maxv = stack[0][0]
                maxind = stack[0][1]

            if nums[i] >= maxv:
                # Clear the stack when a new maximum is found
                stack = []
                maxv = nums[i]
                maxind = i
                stack.append((nums[i], i))
            else:
                # Maintain the stack by popping smaller elements from the end
                while stack and nums[i] >= stack[-1][0]:
                    stack.pop()

                # Add the current element to the stack
                stack.append((nums[i], i))

            # Once the window is full, start recording the maximums
            if i >= k - 1:
                ans.append(stack[0][0])

        return ans
