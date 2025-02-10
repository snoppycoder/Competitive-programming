# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        min_ = min(nums)
        max_ = max(nums)
        l = max_ - min_ + 1
        arr = [0] * l
        res = []
        for num in nums:
            arr[num - min_ ] += 1

        for i in range(len(arr)):
           
            res.extend([i+min_]* arr[i])
        return res

