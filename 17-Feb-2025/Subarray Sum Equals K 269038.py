# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
       
        
        prefixSum = [0]*(len(nums)+1)
        for i in range(len(nums)):
            prefixSum[i+1] = prefixSum[i] + nums[i]
        ds = defaultdict(int)
        ds[0] = 1
        res = 0
        for i in range(len(nums)):
            if prefixSum[i+1] - k in ds:
                res += ds[prefixSum[i+1] - k ]

            ds[prefixSum[i+1]] +=1


   
        return res
            
       

        
            


        