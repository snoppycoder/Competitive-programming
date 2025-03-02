# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        counter = 0  # Count modifications
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:  # Found a decreasing pair
                counter += 1
                if counter > 1:
                    return False  # More than one modification needed
                
                # Modify the correct value
                if i == 0 or nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1]  # they are increasing pairs 
                else:
                    nums[i + 1] = nums[i] 

        return True
