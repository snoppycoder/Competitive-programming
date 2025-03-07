# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        s = path.split("/")
        print(s)
        for char in s:
            if char and char != "." and char != ".." :
                stack.append(char)
            elif stack and char == "..":
                stack.pop() 
        return "/" + "/".join(stack)




        