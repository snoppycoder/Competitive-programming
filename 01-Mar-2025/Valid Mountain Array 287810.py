# Problem: Valid Mountain Array - https://leetcode.com/problems/valid-mountain-array/description/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        idx = 0
        if len(arr) < 3:
            return False
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] > 0 :
                idx = i+1
            elif arr[i+1] - arr[i] <= 0:
                break
        if idx < len(arr)-1 and idx != 0:
            for i in range(idx, len(arr)-1):
                if arr[i] - arr[i+1] <= 0:
                    return False
            return True
        return False
                    




            

        


        