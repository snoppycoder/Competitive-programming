# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:

    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = -1
        for i in range(len(arr)-1, -1, -1):
            new_val = max_val
            max_val = max(max_val, arr[i])
            arr[i] = new_val
        return arr

        
        
        
       