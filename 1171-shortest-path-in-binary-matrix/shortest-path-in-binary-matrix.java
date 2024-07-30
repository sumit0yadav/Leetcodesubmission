import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;
        if (n == 0) return -1;
        int m = grid[0].length;
        
        if (grid[0][0] == 1 || grid[n-1][m-1] == 1) {
            return -1;
        }
        
        int[][] directions = {{1, 1}, {1, 0}, {1, -1}, {0, -1}, {0, 1}, {-1, 1}, {-1, 0}, {-1, -1}};
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[] {0, 0});
        grid[0][0] = 2;  // Mark as visited
        int pathLength = 0;
        
        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            pathLength++;
            for (int i = 0; i < levelSize; i++) {
                int[] cell = queue.poll();
                int x = cell[0];
                int y = cell[1];
                
                if (x == n - 1 && y == m - 1) {
                    return pathLength;
                }
                
                for (int[] direction : directions) {
                    int xx = x + direction[0];
                    int yy = y + direction[1];
                    
                    if (xx == n - 1 && yy == m - 1) {
                        return pathLength + 1;
                    }
                    
                    if (inGrid(xx, yy, n, m) && grid[xx][yy] == 0) {
                        queue.offer(new int[] {xx, yy});
                        grid[xx][yy] = 2;  // Mark as visited
                    }
                }
            }
        }
        
        return -1;
    }
    
    private boolean inGrid(int x, int y, int n, int m) {
        return 0 <= x && x < n && 0 <= y && y < m;
    }
}
