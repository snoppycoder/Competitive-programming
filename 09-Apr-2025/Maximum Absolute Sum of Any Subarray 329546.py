# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        positive = 0
        negative = 0
        res = 0
        for i in range(len(nums)):
            positive += nums[i]
            negative += nums[i]
            if positive < 0:
                positive = 0
            if negative > 0:
                negative = 0

            res = max(abs(positive), abs(negative), res)

        return res

            
        
        