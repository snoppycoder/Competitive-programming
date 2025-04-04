# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def isValid(k):
            a = [0] * (len(nums) + 1)

            for i in range(k):
                l,r,val = queries[i]

                a[l] -= val
                a[r + 1] += val

            for i in range(1, len(a)):
                a[i] += a[i-1]


            for i in range(len(nums)):
                if a[i] + nums[i] > 0:
                    return False

            return True

        solution = -1 
        low,high = 0,len(queries)

        while low <= high:
            mid = low + (high-low)//2
            if isValid(mid):
                solution = mid 
                high = mid - 1
            else:
                low = mid + 1

        return solution


        