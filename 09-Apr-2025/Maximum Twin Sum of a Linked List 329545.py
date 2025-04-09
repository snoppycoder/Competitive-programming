# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        dummy = ListNode(-1, next=None)
        curr = dummy

        while stack:
            node = ListNode(stack.pop())
            curr.next = node
            curr = curr.next
        curr = dummy.next
        curr2 = head
        m = 0
        while curr:
            m = max(m, (curr.val + curr2.val))
            curr2 = curr2.next
            curr = curr.next
        return m





        