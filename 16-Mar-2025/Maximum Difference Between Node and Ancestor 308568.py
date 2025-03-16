# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(node, max_val, min_val):
            if not node:
                return max_val - min_val
            max_val = max(max_val, node.val)
            min_val = min(min_val, node.val)
            left = helper(node.left, max_val, min_val)
            right = helper(node.right, max_val, min_val)
            return max(right, left)
        return helper(root, root.val, root.val)
            
        