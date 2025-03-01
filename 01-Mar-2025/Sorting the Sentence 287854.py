# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        res = ['']*len(s)
        for i in range(len(s)):
            idx =int(s[i][-1])
            res[idx-1] = s[i][:len(s[i])-1]


        return " ".join(res)


        

        