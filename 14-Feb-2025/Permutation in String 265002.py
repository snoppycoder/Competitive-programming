# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        window = Counter()
        left= 0
        for right in range(len(s2)):
            window[s2[right]] += 1
            if (right - left + 1 > len(s1)):
                window[s2[left]] -= 1
                if(window[s2[left]] == 0):
                    del window[s2[left]]
                left += 1
                
            if target == window:
                return True
        return False

        