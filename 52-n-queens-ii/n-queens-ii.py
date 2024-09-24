class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def validate(board,row,col):
            for i in range(n):
                if board[row][i]=='Q':return False
            for i in range(n):
                if board[i][col]=='Q':return False
            i,j=row,col
            while i>=0 and j>=0:
                if board[i][j]=='Q':return False
                i-=1
                j-=1
            i,j=row,col
            while i<n and j<n:
                if board[i][j]=='Q':return False
                i+=1
                j+=1
            i,j=row,col
            while i>=0 and j<n:
                if board[i][j]=='Q':return False
                i=i-1
                j+=1
            i,j=row,col

            while i<n and j>=0:
                if board[i][j]=='Q':return False
                i=i+1
                j-=1
            return True

        
        def dfs(col,board,res):
            if col==n:
                res[0]+=1
                return
            for row in range(n):
                if validate(board,row,col):
                    board[row][col]='Q'
                    dfs(col+1,board,res)
                    board[row][col]='.'
            return


        board=[['.']*n for _ in range(n)]
        res=[0]
        # for col in range(n):
        dfs(0,board,res)
        return res[0]




        