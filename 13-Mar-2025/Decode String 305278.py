# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:

           
    def decodeString(self, s: str) -> str:
        if not s:
            return s
        elif "[" not in s:
            return s

        if s[0] == "[":
            s = s[1:-1]
        
        
        o = 0
        answer = []
        current = []
        i = 0
        n = 0
        flag = True
        while i < len(s):
            if o == 0 and s[i].isdigit():
                digits = ""
                while s[i].isdigit():
                    digits += s[i]
                    i += 1
                n = int(digits)
                flag = False
            
            if flag:
                answer.append(s[i])
            elif s[i] == "[":
                o += 1
            elif s[i] == "]":
                o -= 1
            
            if not flag:
                current.append(s[i])
            if o == 0:
                answer += n * self.decodeString(current)
                n = 1
                current = []
            
            

            i += 1

        return "".join(answer)