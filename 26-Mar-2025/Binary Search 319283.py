# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        for i in range(len(nums)):
            mid = (left + right)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                return mid
            else:
                left = mid + 1
        return -1

        