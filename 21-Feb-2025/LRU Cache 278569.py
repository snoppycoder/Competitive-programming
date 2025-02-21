# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node():
    def __init__(self, key, value, next=None, prev=None):
        self.key = key
        self.value = value
        self.next=  next
        self.prev = prev
    


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.pointers = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

        

    def get(self, key: int) -> int:
        if key in self.pointers:
            node = self.pointers[key]
            self.remove(node)
            self.insertAtTail(node)
            return node.value
        return -1
    def insertAtTail(self, new_node):
        real_tail = self.tail.prev
        real_tail.next = new_node
        new_node.prev = real_tail
        new_node.next = self.tail
        self.tail.prev = new_node
        self.pointers[new_node.key] = new_node
        


    def remove(self, node):
        pr = node.prev
        nxt = node.next
        pr.next = nxt
        nxt.prev = pr 
        self.pointers.pop(node.key)
    def put(self, key: int, value: int) -> None:
        if key in self.pointers:
            new_node = self.pointers[key]
            self.remove(new_node)
            new_node.value = value
        elif len(self.pointers) == self.capacity:
                self.remove(self.head.next)
        new_node = Node(key, value)

        self.insertAtTail(new_node) 
            
        


        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)