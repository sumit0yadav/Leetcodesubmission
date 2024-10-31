from typing import List
from heapq import heappush, heappop

# Define movement directions: right, down, left, up
moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Initialize variables
        N = len(grid) - 1  # grid size - 1 for boundary checking
        i, j = 0, 0  # starting position
        pq = []  # priority queue (min-heap)
        ans = grid[0][0]  # minimum time to reach (0, 0)

        # Main loop to traverse the grid until reaching the bottom-right corner
        while i != N or j != N:
            # Explore all four possible directions
            for a, b in moves:
                ia, jb = i + a, j + b  # new position

                # Continue if the new position is out of bounds or already visited
                if ia < 0 or ia > N or jb < 0 or jb > N or grid[ia][jb] > 2500:
                    continue

                # Push new cell to the priority queue with its elevation as the priority
                heappush(pq, (grid[ia][jb], ia, jb))

                # Mark cell as visited by setting a high value
                grid[ia][jb] = 3000

            # Pop the next cell with the lowest elevation from the priority queue
            elevation, i, j = heappop(pq)

            # Update the answer with the maximum elevation seen so far
            ans = max(ans, elevation)

        return ans
