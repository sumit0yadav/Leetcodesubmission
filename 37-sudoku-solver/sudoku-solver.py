from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solves the Sudoku puzzle in-place using backtracking.
        """
        def valid(board: List[List[str]], irow: int, jcol: int, num: str) -> bool:
            # Check if 'num' can be placed at board[irow][jcol]
            
            # Check the row and column
            for i in range(9):
                if board[irow][i] == num or board[i][jcol] == num:
                    return False

            # Check the 3x3 sub-grid
            start_row, start_col = 3 * (irow // 3), 3 * (jcol // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False
            
            return True
        
        def solve(board: List[List[str]]) -> bool:
            # Try to solve the board using backtracking
            for irow in range(9):
                for jcol in range(9):
                    if board[irow][jcol] == '.':  # Find an empty cell
                        
                        for num in '123456789':  # Try numbers 1-9
                            if valid(board, irow, jcol, num):
                                board[irow][jcol] = num  # Place the number
                                
                                if solve(board):  # Recursive call
                                    return True
                                
                                board[irow][jcol] = '.'  # Backtrack

                        return False  # No valid number leads to a solution
                        
            return True  # Puzzle is solved

        # Call the solve function to modify the board in-place
        solve(board)

# Example usage:
# board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# sol = Solution()
# sol.solveSudoku(board)
# print(board)
