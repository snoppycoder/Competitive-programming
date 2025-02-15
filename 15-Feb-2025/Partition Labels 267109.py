# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []

        max_ = float('-inf')
        last = defaultdict(int)
        window = defaultdict(int)
        # find the last occurance of each letter
        for index, char in enumerate(s):
            last[char] = index
        left = 0

        for right in range(len(s)):
            window[s[right]] = right
            max_ = max(last[s[right]], max_)
            if(right == max_):
                max_ = float('-inf')
                res.append(right-left+1)
                left = right+1
        return res
            

            


        print(last)
        return [0]

        
        