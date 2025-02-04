# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lst = str(int("".join([str(nums) for nums in digits]))+1)
        return [int(nums) for nums in lst]

      
         
        