# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        res = 0
        left, right = 0, len(skill)-1
        target = skill[left] + skill[right]
        while left < right:
            if (skill[left] + skill[right] ) == target:
                res+=(skill[left]*skill[right])
                
            else:
                return -1
            left+=1
            right-=1
       
        
        return res
                
                

        
        