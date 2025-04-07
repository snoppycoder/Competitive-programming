# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []
        curr1 = l1
        curr2 = l2
        while curr1:
            stack1.append(curr1.val)
            curr1 = curr1.next
        while curr2:
            stack2.append(curr2.val)
            curr2 = curr2.next
        stack1 = list(reversed(stack1))
        stack2 = list(reversed(stack2))
        test = stack2 if len(stack1) > len(stack2) else stack1 
        flag = False
        if stack2 == test:
            flag = True

        stack = test.copy()
        ans = [0]
        dummy = ListNode(-1)
        d = 1
        
        while stack:
            stack.pop()
            ans.append(ans[-1] + (stack1.pop() + stack2.pop())*d)
            d *= 10
        if flag:
            while stack1:
                ans.append(ans[-1] + (stack1.pop())*d)
                d *= 10
        else:
            while stack2:
                ans.append(ans[-1] + (stack2.pop())*d )
                d *= 10
        total = str(ans[-1])
        total = total[::-1]
        print(total)
        curr = dummy
        for i in range(len(total)):
            curr.next = ListNode(int(total[i]))
            curr = curr.next
        return dummy.next
        
        
