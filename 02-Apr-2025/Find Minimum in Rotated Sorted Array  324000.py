# Problem: Find Minimum in Rotated Sorted Array  - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 0, n -  1
        min_val = float('inf')
    
        while low < high:
            mid = (low + high)//2
            if nums[mid] > nums[high]:
                low = mid + 1
                 
            else:
                high = mid 
            
               
            
        return nums[low]



        