# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        res = float('-inf')
        for i in range(len(nums)-2):
            if nums[i+1] + nums[i+2] > nums[i]:
                res = max(res, nums[i+1] + nums[i+2] + nums[i])
        if res == float('-inf'):
            return 0
        return res
