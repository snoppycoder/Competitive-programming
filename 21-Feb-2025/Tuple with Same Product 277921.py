# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        ds = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
               
               
                ds[nums[i]*nums[j]] +=1
       
       
        res = 0
        for count in ds.values():
            if count > 1:
                res+= ((count * (count-1))//2)*8
        return res
