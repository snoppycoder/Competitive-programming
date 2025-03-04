# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ds = defaultdict(int)
        res = 0
        for num in answers:
            ds[num+ 1] += 1
            if ds[num+1] == num + 1:
                # print(ds)
                res += num+ 1
                ds[num+ 1] = 0
                print(ds)
               
        for key in ds:
            if ds[key] > 0:
                res += key
        
        return res

        