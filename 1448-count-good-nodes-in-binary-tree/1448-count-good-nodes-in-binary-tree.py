# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        max_value = root.val
        stack = [(root, max_value)]
        count = 0
        while stack:
            cur, max_value = stack.pop()
            if cur.val >= max_value:
                count += 1
                max_value = cur.val
            if cur.left:
                stack.append( (cur.left, max_value) )
            if cur.right:
                stack.append( (cur.right, max_value) )
        return count
                
