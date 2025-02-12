# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
    
        index = 0
        for i in range(len(costs)):
            if(coins >= costs[i]):
                coins -= costs[i]
                index +=1
            else:
                break
        return index
       
    
        
    
        
        
                

        