# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count+=1
                res =max(res, count)
            else:
                count = 0
        return res

                