# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        arr = self.getRow(rowIndex-1)
        res = [1]
        for i in range(len(arr)-1):
            res.append(arr[i] + arr[i+1])
        res.append(1)
        return res
            
