# Problem: 3 Sum Closest - https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort() 
        res = float('inf')
        total = 0 


        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < abs(res- target):
                    res = total
                if total < target:
                    left+=1
                elif total > target:
                    right-=1
                else:
                    return total
        return res

        


        

        