# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            curr = [root]
            h = 0
            while curr:
                new = []
                values = []
                for node in curr:
                    if node.left:
                        new.append(node.left)
                        values.append(node.left.val)
                    if node.right:
                        new.append(node.right)
                        values.append(node.right.val)
                
                if h % 2 == 0:
                    rev = list(reversed(values))
                    i = 0
                    for node in curr:
                        if node.left:

                            node.left.val = rev[i]
                            i+=1
                        if node.right:
                            node.right.val = rev[i]
                            i+=1

                
                curr = new
                h += 1
               
            return root
        return helper(root)





        