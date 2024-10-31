from typing import List
from heapq import heappush, heappop

# Define movement directions: right, down, left, up
moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        N = len(grid) - 1  
        i, j = 0, 0  
        pq = []  
        ans = grid[0][0] 

        while i < N or j < N:
            for a, b in moves:
                ia, jb = i + a, j + b  # new position

                if ia < 0 or ia > N or jb < 0 or jb > N or grid[ia][jb] > 2500:
                    continue

                
                heappush(pq, (grid[ia][jb], ia, jb))

                grid[ia][jb] = 3000

            elevation, i, j = heappop(pq)

            ans = max(ans, elevation)

        return ans
