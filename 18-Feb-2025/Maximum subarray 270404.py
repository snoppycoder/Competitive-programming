# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        res = float('-inf')
        curr =0
        for i in range(len(arr)):
            if curr < 0:
                curr = 0
            curr += arr[i]
            res = max(res, curr)
        return res


        
