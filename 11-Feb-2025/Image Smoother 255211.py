# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        res = [[0]*cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                total, count = 0,0 
                for i in range(r-1, r+2):
                    for j in range(c-1, c+2):
                        if i < 0 or j < 0 or i == len(img) or j == len(img[0]):
                            continue
                        total += img[i][j]
                        count += 1
                res[r][c] = total // count
        return res


        