# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res=  []
        for keys, values in count.items():
            if(values == 2):
                res.append(keys)
        return res
        