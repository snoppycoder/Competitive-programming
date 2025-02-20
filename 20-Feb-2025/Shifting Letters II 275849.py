# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ascii_val = [ord(char)-ord('a') for char in s]
        event = [0]*(len(s)+1)
        word = []
        for start, end, direction in shifts :
            if direction == 1:
                event[start] +=1
                event[end+1] -=1
            else:
                event[start] -=1
                event[end+1] +=1
        for i in range(1, len(event)):
            event[i] += event[i-1]
        for i in range(len(ascii_val)):
            val = (ascii_val[i] + event[i])%26
            word.append(chr(val + ord('a')))
           

        
        return "".join(word)


       