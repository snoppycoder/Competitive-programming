# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        curr = [root]
        level = 1
        res = [[root.val]]
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
            if level % 2  == 1 and values:
                res.append(list(reversed(values)))
            elif level % 2 == 0 and values:
                res.append(values)
            level += 1
            curr = new
        return res

        