# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        res= ['0']*len(s)
        count = 0
        one = s.count('1')
        zero = s.count('0')
        for i in range(one-1):
            res[i] = '1'
        res[-1] = '1'
        return "".join(res)