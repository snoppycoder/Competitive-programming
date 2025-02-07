# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        res = []
        s = s.split()
        word = ""
        n = max([len(word) for word in s])
        for i in range(n):
            for j in range(len(s)):
                
                if i < len(s[j]):
                    word += s[j][i]
                else:
                    word += " "
                    
                
            res.append(word.rstrip())
            word = ""
        return res
                    
        