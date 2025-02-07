# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        dict_ = {
            "first":"qwertyuiop",
            "second": "asdfghjkl",
            "third": "zxcvbnm"
        }

        for word in words:
            first = word[0].lower()
            if first in dict_['first']:
                row = "first"
            elif first in dict_['second']:
                row = "second"
            else:
                row = "third"

            for letter in word:
                if letter.lower() not in dict_[row]:
                    break
            else:
                res.append(word)

        return res
            

        