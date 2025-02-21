# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.data_map = {}
        self.data_list = []
        

    def insert(self, val: int) -> bool:
        if val in self.data_map:
            return False
        self.data_map[val] = len(self.data_list)
        self.data_list.append(val)
        return True
        
        

    def remove(self, val: int) -> bool:
        if val not in self.data_map:
            return False
        index = self.data_map[val]
        last_element = self.data_list[-1]
        self.data_list[index] = last_element
        self.data_map[last_element] = index
        self.data_list.pop()
        del self.data_map[val] 
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.data_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()