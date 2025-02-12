# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            counter = 0
            for i in range(len(nums)):
                if(nums[i] < num):
                    counter+=1
            res.append(counter)
        return res
                
        