# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        freq = [0]*(len(nums))
        for start, end in requests:
            freq[start] +=1
            if end + 1 < len(nums):
                freq[end+1] -=1
        ps = [freq[0]]*len(freq)
        for i in range(1, len(freq)):
            ps[i] = ps[i-1] + freq[i]
        ps.sort(reverse=True)
        nums.sort(reverse=True)
        res = 0
        for i in range(len(nums)):
            res +=( nums[i] * ps[i])
        return res % (10**9 + 7)

        