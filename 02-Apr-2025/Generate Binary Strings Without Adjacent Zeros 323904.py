# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        res, sol = [], []
        def helper():
            if len(sol) == n:
                res.append("".join(sol))
                return
            if not sol or sol[-1] != "0":
                sol.append("0")
                helper()
                sol.pop()
            
            sol.append("1")
            helper()
            sol.pop()

        helper()
        return res  
        
           