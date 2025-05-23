# Problem: First Bad Version - https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        high  = n 
        while low <= high:
            mid = (low + high)//2
            if not isBadVersion(mid):
                low = mid + 1
            else:
                high = mid - 1
        return low

        