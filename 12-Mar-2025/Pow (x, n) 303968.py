# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # xself.myPow(x, n -1)
        if(n==0):
            return 1
        if n < 0:
            return 1/(self.myPow(x, -n))
        half = self.myPow(x, n//2)
        if n % 2 == 0:
           return half * half
        else:
           return x * half * half

        