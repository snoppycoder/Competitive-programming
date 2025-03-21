# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
            return arr
        
        inorder(root)

        def solve(arr):
            if len(arr) == 0:
                return None
            median = len(arr)//2
            root = TreeNode(arr[median])
            root.left = solve(arr[:median])
            root.right = solve(arr[median+1:])
            return root
        
        print(arr)
        return solve(arr)



        