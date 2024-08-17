class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []
        nQueens = ['.' * n for _ in range(n)]
        self.solveNQueensHelper(res, nQueens, 0, n)
        return res

    def solveNQueensHelper(self, res, nQueens, row, n):
        if row == n:
            res.append(list(nQueens))
            return
        for col in range(n):
            if self.isValid(nQueens, row, col, n):
                nQueens[row] = nQueens[row][:col] + 'Q' + nQueens[row][col+1:]
                self.solveNQueensHelper(res, nQueens, row + 1, n)
                nQueens[row] = nQueens[row][:col] + '.' + nQueens[row][col+1:]

    def isValid(self, nQueens, row, col, n):
        # Check if the column had a queen before.
        for i in range(row):
            if nQueens[i][col] == 'Q':
                return False
        # Check if the 45° diagonal had a queen before.
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if nQueens[i][j] == 'Q':
                return False
        # Check if the 135° diagonal had a queen before.
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if nQueens[i][j] == 'Q':
                return False
        return True
