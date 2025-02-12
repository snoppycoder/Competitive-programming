# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left, right = 0, len(people)-1
        people.sort()
        res = 0
        while (left <= right):
            if(people[left] + people[right] <= limit):
                # if you have some space
                left += 1
            right-=1
            res+=1
        




        return res 