# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r = l= res = 0
        for char in s:
            if char == 'R':
                r += 1
            else:
                l+=1
            if r == l:
                res +=1
        return res

