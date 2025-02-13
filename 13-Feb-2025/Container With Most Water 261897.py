# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        res = 0
        while left < right:
            if height[left] < height[right]:
                res = max(res, (right-left)*height[left])
                left+=1

            else:
                res = max(res, (right-left)*height[right])
                right-=1
        return res