# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def flip(left, right):
            while(left< right):
                nums[left], nums[right] = nums[right], nums[left]
                right-=1
                left+=1

        if(len(nums) == 1):
            return 
        k = k % len(nums)
            
        flip(0, len(nums)-1)# reverse
        flip(0, k-1)
        flip(k, len(nums)-1)
