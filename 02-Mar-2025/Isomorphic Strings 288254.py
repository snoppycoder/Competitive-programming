# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ds = defaultdict()
        for i in range(len(s)):
            if s[i] not in ds and t[i] not in ds.values(): 
                ds[s[i]] = t[i]
            elif t[i] in ds.values() and s[i] not in ds:
                return False

            else:
                if ds[s[i]] != t[i]:
                    return False
        return True