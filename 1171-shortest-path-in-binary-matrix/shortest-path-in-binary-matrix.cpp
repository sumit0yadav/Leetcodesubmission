#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        
        // Check if start or end cell is blocked
        if (grid[0][0] == 1 || grid[n-1][m-1] == 1) {
            return -1;
        }
        
        // Direction vectors for 8 possible moves
        vector<pair<int, int>> delta = {
            {1, 1}, {1, 0}, {1, -1}, {0, -1}, {0, 1},
            {-1, 1}, {-1, 0}, {-1, -1}
        };
        
        // Queue for BFS
        queue<pair<int, int>> q;
        q.push({0, 0});
        grid[0][0] = 2; // Mark the starting cell as visited
        int ans = 1;
        
        // BFS traversal
        while (!q.empty()) {
            int levelSize = q.size();
            for (int i = 0; i < levelSize; ++i) {
                int x = q.front().first;
                int y = q.front().second;
                q.pop();
                
                // Check if we reached the bottom-right corner
                if (x == n - 1 && y == m - 1) {
                    return ans;
                }
                
                // Explore all 8 possible directions
                for (const auto& d : delta) {
                    int xx = x + d.first;
                    int yy = y + d.second;
                    
                    if (xx == n - 1 && yy == m - 1) {
                        return ans + 1;
                    }
                    
                    // Check if the next cell is within grid bounds and not visited
                    if (xx >= 0 && xx < n && yy >= 0 && yy < m && grid[xx][yy] == 0) {
                        grid[xx][yy] = 2; // Mark the cell as visited
                        q.push({xx, yy});
                    }
                }
            }
            ++ans;
        }
        
        return -1; // Return -1 if no path found
    }
};
