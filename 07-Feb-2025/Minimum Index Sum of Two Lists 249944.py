# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:      
        minimum = float('inf')
        res = []
        dict_ = defaultdict(int)
        for word in list1:
            for word2 in list2:
                if(word == word2):
                    dict_[word] = list1.index(word) + list2.index(word2)
        for keys, values in dict_.items():
            if(minimum > values):
                minimum = values
        for keys, values in dict_.items():
            if(values == minimum):
                res.append(keys)
        

        return res




