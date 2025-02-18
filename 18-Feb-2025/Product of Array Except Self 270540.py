# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ps = [nums[0]] * len(nums)
        ss = [nums[-1]] * len(nums)
        res = []
        for i in range(1, len(nums)):
            ps[i] = nums[i] * ps[i-1]
        nums.reverse()
        for i in range(1, len(nums)):
            ss[i] = nums[i] * ss[i-1]
        ss.reverse()
        for i in range(len(nums)):
            if i == 0:
                res.append(ss[i+1])
           
            elif i == len(nums)-1:
                res.append(ps[i-1])
            else:
                res.append(ss[i+1]*ps[i-1])
        print(ss, ps)
        return res


        
            

       
        