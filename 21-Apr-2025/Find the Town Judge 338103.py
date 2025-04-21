# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        d = defaultdict(list)
        for t, e in trust:
            d[t].append(e)
            
        res = 0
        t = []
        for key, val in d.items():
            t.extend(val)
        c = Counter(t)
        print(c)
        if len(trust) == 0:
            return 1 if n == 1 else -1
        for key, val in c.items():
            if val == n-1 and key not in d:
                return key
        return -1


        

        