# Problem: Linked List Cycle - https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        dummy = ListNode(-1)
        dummy.next= head
        slow = dummy
        count = 0
        while fast != slow and fast and fast.next:  
            fast = fast.next.next
            slow = slow.next
        if fast== None or fast.next == None:
            return False
        return True
        


        
        