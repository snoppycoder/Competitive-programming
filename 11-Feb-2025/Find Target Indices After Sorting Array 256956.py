# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        max_ = max(nums)
        min_ = min(nums)
        l = max_ - min_ + 1
        res = [0] * l
        s = []
        ans = []
        for num in nums:
            res[num - min_ ] += 1
        for i in range(len(res)):
            s.extend([i + min_]* res[i])

        for i in range(len(s)):
            if s[i] == target:
                ans.append(i)
        return ans



        