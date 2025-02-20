# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
      
        dummy = ListNode()
        res  = dummy
        curr = head
        prev = None
        while curr:
            if curr.val < x:
                dummy.next = curr
                dummy = dummy.next
                if prev:
                    prev.next = curr.next
                if curr == head:
                    head = curr.next
                curr = curr.next
            else:  
                prev = curr
                curr = curr.next
        dummy.next = head
        return res.next
            


       