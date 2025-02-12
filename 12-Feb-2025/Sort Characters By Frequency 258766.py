# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        counter = dict(sorted(counter.items(), key= lambda item: item[1], reverse=True))
        word = ""
        for keys, values in counter.items():
           word+=str(keys*values)
        return "".join(word)   

        