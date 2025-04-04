# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def isValid(num):
            f = position[0]
            count = 1
            for i in range(1, len(position)):
                if position[i] - f >= num:
                    count += 1
                    f = position[i]

                if count == m:
                    return True
            return False


        position.sort()
        low, high = 1, position[-1]- position[0]
        sol = -1
        while low <= high:
            mid = (low + high)//2
            if isValid(mid):
                sol = mid
                low = mid + 1
            else:
                high = mid - 1
        return sol



        