# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            j = i+1
            if(nums[i] == nums[j]):
                nums[i]*=2
                nums[j] = 0
    
        #shifting the zeros
        holder = 0
        for seeker in range(len(nums)):

            if nums[seeker] != 0:
                #positive
                nums[seeker], nums[holder] = nums[holder], nums[seeker]
                holder += 1

        return nums
        