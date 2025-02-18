# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        cols = len(matrix[0])
        rows = len(matrix)
        self.ps = [[0]*(cols+1) for _ in range(rows+1)]
        for i in range(1, len(self.ps)):
            for j in range(1, len(self.ps[i])):
                self.ps[i][j] = self.ps[i-1][j] + self.ps[i][j-1] - self.ps[i-1][j-1] + matrix[i-1][j-1]
     
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # obj = NumMatrix(matrix)
        ps = self.ps
        return ps[row2+1][col2+1] -ps[row1][col2+1] - ps[row2+1][col1] + ps[row1][col1] 
        


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)