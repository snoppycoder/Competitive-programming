# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        count = Counter(chars)
        
        for word in words:
            copy = count.copy()
            breaked = False
            for char in word:
                if(char in copy and copy[char] > 0):
                    copy[char] -= 1
                else:
                    breaked = True
                    break
            if not breaked:
            
                res += len(word)
        return res



