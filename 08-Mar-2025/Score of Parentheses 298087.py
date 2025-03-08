# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack  = [0]
        score = 0
        for char in s:
            if char == "(":
                stack.append(0)
            else:
                top = stack.pop()
                score = max(2*(top), 1)
                stack[-1] += score
        return stack[0]