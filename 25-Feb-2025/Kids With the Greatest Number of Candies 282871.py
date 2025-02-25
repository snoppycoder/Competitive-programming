# Problem: Kids With the Greatest Number of Candies - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_ = max(candies)
        res = []
        for num in candies:
            if num + extraCandies >= max_:
                res.append(True)
            else:
                res.append(False)
        return res
        