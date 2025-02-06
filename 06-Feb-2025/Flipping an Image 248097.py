# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, images: List[List[int]]) -> List[List[int]]:
        temp = []
        for i in range(len(images)):
            for j in range(len(images[i])-1, -1, -1):
                temp.append(images[i][j])
            images[i] = temp
            temp = []


                
            
        print(images)
        for i in range(len(images)):
            for j in range(len(images[i])):
                if(images[i][j] == 0):
                    images[i][j] = 1
                else:
                    images[i][j] = 0
        return images
        