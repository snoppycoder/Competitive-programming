# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            candidate = [list(row) for row in zip(*mat[::-1])]
            if(candidate == target):
                return True
            mat = candidate
        return False
       