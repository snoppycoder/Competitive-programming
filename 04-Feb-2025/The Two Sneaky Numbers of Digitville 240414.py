# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

from collections import Counter

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res= []

        dict_ = Counter(nums)
        for keys, values in dict_.items():
            if(values == 2):
                res.append(keys)
        return res


