# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for i, step in enumerate(nums): 
            if(step > 0):
                i = (step + i) % n
            elif(step< 0):
                i = (i + step + n) % n

            res.append(nums[i])
            
        return res