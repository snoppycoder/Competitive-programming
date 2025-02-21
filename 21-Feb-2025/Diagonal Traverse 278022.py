# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonal = defaultdict(list)
        rows = len(mat)
        res = []
        cols = len(mat[0])
        for i in range(rows):
            for j in range(cols):
                diagonal[i+j].append(mat[i][j])
        for keys, values in diagonal.items():
            if keys %2 == 0:
                res.extend(reversed(list(values)))
            else:
                res.extend(list(values))
        return res

            

        