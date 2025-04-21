# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        curr = head
        while curr:
            res.append(curr.val)
            curr = curr.next
        res.sort()
        dummy = ListNode(-1)
        curr = dummy
        for num in res:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next

        