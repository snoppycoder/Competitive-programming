# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        full, extra = divmod(time, n - 1)
        if full % 2 == 0:
            return extra + 1
        
        return n - extra

