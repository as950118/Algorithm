# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([ (root, 0) ])
        ret = {}
        while queue:
            cur, depth = queue.popleft()
            if cur == None:
                continue
            ret[depth] = cur.val
            queue.append( (cur.left, depth+1) )
            queue.append( (cur.right, depth+1) )
        return list(ret.values())
            

        