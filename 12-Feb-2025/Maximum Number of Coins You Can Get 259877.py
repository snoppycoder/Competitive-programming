# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        m = 0
        n = len(piles)//3
        for i in range(1, 2*n, 2):
            m += piles[i]
        return m
            
