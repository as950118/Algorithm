# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([ (root,1) ])
        max_to_level = {}
        while queue:
            cur, depth = queue.popleft()
            if cur == None:
                continue
            if depth in max_to_level:
                max_to_level[depth] += cur.val
            else:
                max_to_level[depth] = cur.val
            queue.append( (cur.left, depth+1) )
            queue.append( (cur.right, depth+1) )
        max_level = 0
        max_val = -float('inf')
        for k, v in max_to_level.items():
            if max_val < v:
                max_val = v
                max_level = k
        return max_level
