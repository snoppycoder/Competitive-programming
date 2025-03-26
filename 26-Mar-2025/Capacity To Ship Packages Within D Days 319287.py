# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def helper(capacity):
            total = 0
            day = 1
            for weight in weights:
                if total + weight > capacity:
                    day += 1
                    total = weight
                else:
                    total += weight
            return days >= day
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right )//2
            if helper(mid):
                right = mid
            else:
                left = mid + 1
        return left



        