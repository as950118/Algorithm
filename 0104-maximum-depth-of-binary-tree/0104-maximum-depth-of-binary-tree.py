# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        cur = root
        depth = 1
        stack = [[cur, depth]]
        ret = 0
        while stack:
            cur, depth = stack.pop()
            if not cur:
                continue
            stack.append([cur.left, depth+1])
            stack.append([cur.right, depth+1])
            ret = max(ret, depth)
        return ret
        # n = len(root)
        # depth = 0
        # i = 0
        # while i<n:
        #     i += 2**depth
        #     depth +=1
        # return depth
