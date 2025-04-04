# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            low, high = 0, len(matrix[i])-1
            while low <= high:
                mid = (high+low)//2
                if matrix[i][mid] > target:
                    high = mid - 1
                elif matrix[i][mid] == target:
                    return True
                else:
                    low = mid + 1
        return False
                    

            
        