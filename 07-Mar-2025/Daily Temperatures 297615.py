# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ds = defaultdict(int)
        stack = []
        ans = [0]*len(temperatures)
        for i in range(len(temperatures)):
        
            while stack and temperatures[stack[-1]] < temperatures[i]:
                n = stack.pop()
                ans[n] = i - n
            stack.append(i)
        return ans