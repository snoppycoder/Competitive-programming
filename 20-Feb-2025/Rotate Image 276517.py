# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix) ):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        right = len(matrix)-1
        left = 0
        print(matrix)
        for i in range(len(matrix)):
            
            while left < right:
                matrix[i][left] , matrix[i][right] = matrix[i][right], matrix[i][left]
                left+=1
                right-=1
            left = 0
            right = len(matrix[i])-1
           
        return matrix
                
    
            

