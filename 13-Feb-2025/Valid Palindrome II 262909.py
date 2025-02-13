# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        right = len(s)-1
        left = 0
        counter = Counter(s)
        left_removed = 0
        right_removed= 0
        
        while (left < right):
            if(s[left] == s[right]):
                left+=1
                right-=1
            else:
                right_removed +=1
                right-=1
        left = 0
        right = len(s)-1
        while(left < right):
             if(s[left] == s[right]):
                left+=1
                right-=1
             else:
                left_removed +=1
                left+=1
        minimum = min(left_removed, right_removed)
        if (minimum > 1):
            return False
        return True