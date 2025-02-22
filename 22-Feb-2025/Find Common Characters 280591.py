# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        common_word = Counter(words[0])
        for word in words[1:]:
            common_word&=Counter(word)
        return list(common_word.elements())