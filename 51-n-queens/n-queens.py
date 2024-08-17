class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def solve(n):
            res=[]

            nqueens=['.'* n for _ in range(n) ]

            

            def solvehelper(res,nqueens,row,n):

                if row==n:
                    res.append(list(nqueens))
                    return
                for col in range(0,n):
                    if valid(nqueens,row,col,n):
                        nqueens[row]=nqueens[row][:col]+'Q'+nqueens[row][col+1:]
                        solvehelper(res,nqueens,row+1,n)
                        nqueens[row]=nqueens[row][:col]+'.'+nqueens[row][col+1:]
            
            def valid(nqueens,row,col,n):
                for i in range(row):
                    if nqueens[i][col]=='Q':
                        return False
                for i,j in zip(range(row-1,-1,-1),range(col-1,-1,-1)):
                    if nqueens[i][j]=='Q':
                        return False
                for i,j in zip(range(row-1,-1,-1),range(col+1,n)):
                    if nqueens[i][j]=='Q':
                        return False
                return True

            solvehelper(res,nqueens,0,n)
            return res
        
        return solve(n)
        