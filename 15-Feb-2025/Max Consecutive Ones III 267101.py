# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        res = 0
        counter=  defaultdict(int)
        for right in range(len(nums)):
            counter[nums[right]] +=1
            while(counter[0] > k):
                # invalid
                counter[nums[left]] -=1
                left+=1
            res = max(res, right-left+1)
        return res
        
        