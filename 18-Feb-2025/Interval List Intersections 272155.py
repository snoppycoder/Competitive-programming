# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        left = 0
        res = []
        right = 0
        while left < len(firstList) and right < len(secondList):
            start = max(firstList[left][0], secondList[right][0])
            end = min(firstList[left][1], secondList[right][1])
            if (start <= end):
                res.append([start, end])
            if firstList[left][1] > secondList[right][1]:
                right+=1
            else:
                left +=1
        return res
            

       
            
        