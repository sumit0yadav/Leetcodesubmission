class Solution:
    import copy
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def count(grid,i,j):
            ch=0
            dir=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

            for dx,dy in dir:
                if 0<=i+dx<len(grid) and 0<=j+dy<len(grid[0]):
                    ch+=grid[i+dx][j+dy]
            return ch

        grid=copy.deepcopy(board)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and count(grid,i,j)<2:
                    board[i][j]=0
                elif grid[i][j]==1 and (2<=count(grid,i,j)<=3):
                    board[i][j]=1
                elif grid[i][j]==1 and count(grid,i,j)>3:
                    board[i][j]=0
                elif grid[i][j]==0 and count(grid,i,j)==3:
                    board[i][j]=1

        