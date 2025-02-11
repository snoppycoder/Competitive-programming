# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(len(nums) - i -1):
                if str(nums[j+1]) + str(nums[j]) > str(nums[j]) + str(nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        if (all((num ==0) for num in nums)):
            return "0"
        return "".join(map(str, nums))


        