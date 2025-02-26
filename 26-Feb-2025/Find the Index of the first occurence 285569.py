# Problem: Find the Index of the first occurence - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == haystack:
            return 0
        if needle in haystack:
            for i in range(len(haystack)):
                if haystack[i] == needle[0] and i + len(needle) <= len(haystack):
                    if haystack[i:i+len(needle)] == needle:
                        return i
            return -1

        else:
            return -1

        