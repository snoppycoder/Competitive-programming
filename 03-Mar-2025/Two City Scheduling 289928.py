# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:

    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        x = sorted(costs, key=lambda item: item[0]- item[1])
        res = 0
        for i in range(len(costs)//2):
            res+=x[i][0]
        for j in range(len(costs)//2, len(costs)):
            res += x[j][1]
        return res


        


        
        