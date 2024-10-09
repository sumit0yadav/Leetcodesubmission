class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def makezero(matrix,row,col):
            rows=len(matrix)
            cols=len(matrix[0])

            for i in range(rows):
                matrix[i][col][1]=0
            for i in range(cols):
                matrix[row][i][1]=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                x=matrix[i][j]
                matrix[i][j]=[x,x]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j][0]==0:
                    makezero(matrix,i,j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                matrix[i][j]=matrix[i][j][1]


        