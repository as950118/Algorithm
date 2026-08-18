# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        paths = [
            (root, 0),            
            ]
        stack = [(root, 0)]
        while paths:
            cur, _ = paths.pop()
            if cur.left:
                paths.append( (cur.left, 0) )
                stack.append( (cur.left, 0) )
            if cur.right:
                paths.append( (cur.right, 0) )
                stack.append( (cur.right, 0) )
        ret = 0
        while stack:
            cur, perfix_sum = stack.pop()
            if cur is None:
                continue
            if perfix_sum + cur.val == targetSum:
                ret += 1            
            stack += [
                (cur.left, perfix_sum + cur.val), 
                (cur.right, perfix_sum + cur.val),
            ]
        return ret