# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = 0
        temp = k
       
        i = 0
        while temp > 0:
            res += nums[i]
            i+=1
            temp-=1
    
        left = 0
        right = k
        res2 = res
        while right< len(nums):
            res2 = res2- nums[left] + nums[right]
            print(res2)
            if (res < res2):
                res = res2
            left+=1
            right+=1
        return res/k
            
             
        