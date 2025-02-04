# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        seen = set()
        # populate the set 
        for i in range(len(ranges)):
            for n in range(ranges[i][0], ranges[i][1]+1):
                seen.add(n)
        
        for i in range(left, right+1):
            if(i not in seen):
                return False
        return True



                


        