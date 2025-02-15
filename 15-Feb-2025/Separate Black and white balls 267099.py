# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        holder = 0
        s = list(s)
        res = 0
        
        for seeker in range(len(s)):
            
                if s[seeker] == '0':
                    s[holder], s[seeker] = s[seeker], s[holder]
                    res += seeker - holder
                    holder+=1
            

                    
                
        return res
        