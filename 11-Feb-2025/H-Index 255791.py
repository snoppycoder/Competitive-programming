# Problem: H-Index - https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort(reverse =True)
        h = 0
        for  index, value in enumerate(citations):
            if(value >= index + 1):
                h = index+ 1
            else:
                return h
        return h


       
            




            
