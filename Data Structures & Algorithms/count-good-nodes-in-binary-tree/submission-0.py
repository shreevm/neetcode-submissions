# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    
        def dfs(node,max_no):
            if not node:
                return 0
            good= 1 if node.val>=max_no else 0
            max_no=max(max_no,node.val)
            good+=dfs(node.left, max_no)
            good+=dfs(node.right,max_no)
            return good
 
        return dfs(root,float('-inf')) 