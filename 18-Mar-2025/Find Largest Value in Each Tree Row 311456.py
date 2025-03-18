# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, level):
    
            if not node:
                return
            # if level == len(res):
            #     # unencountered level
            #     res.append([])
            lev_max[level] = max(lev_max[level], node.val)
            dfs(node.left, level + 1)       
            dfs(node.right, level + 1)     
        
        ans = []
        lev_max = defaultdict(lambda : float('-inf'))
        dfs(root, 0)
        for level, mx in lev_max.items():
            ans.append(mx)
        return ans
    