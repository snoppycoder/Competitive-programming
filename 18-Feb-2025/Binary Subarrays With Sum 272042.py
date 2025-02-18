# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0
        ds = defaultdict(int)
        ds[0] = 1
        ps = 0
        for num in nums:
            ps += num
            if ps-goal in ds:
                res += ds[ps-goal]

            ds[ps] +=1
        return res


