# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, index, ans=[]):
            if index == len(nums):
                ans.append(nums[::])
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                backtrack(nums, index+1, ans)
                nums[index], nums[i] = nums[i], nums[index]
            return ans
        return backtrack(nums, 0, ans=[])
        