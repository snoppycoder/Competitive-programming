# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
        
            if token.lstrip('-').isdigit():
                stack.append(int(token))
            
            else:
                b = stack.pop()
                a = stack.pop()

                if token == "*":
                    stack.append(a * b)
                elif token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                else:
                    stack.append(int(a/b))
               
        return stack[-1]