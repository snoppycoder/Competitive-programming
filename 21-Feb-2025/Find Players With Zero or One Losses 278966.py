# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        player = set()
        l = defaultdict(int)
        for win, lose in matches:
            player.add(win)
            player.add(lose)
            l[lose] +=1
        wins = sorted(list(player ^ l.keys()))
        lost = []
        for keys, values in l.items():
            if values == 1:
                lost.append(keys)
        lost.sort()
        res = []
        res.append(wins)
        res.append(lost)
        return res


    
