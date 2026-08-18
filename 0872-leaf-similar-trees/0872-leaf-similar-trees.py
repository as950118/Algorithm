# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaf(root) -> list:
            leaf = list()
            stack = [root]
            while stack:
                cur = stack.pop()
                if cur.left == None and cur.right == None:
                    leaf.append(cur.val)
                else:
                    if cur.left:
                        stack.append(cur.left)
                    if cur.right:
                        stack.append(cur.right)
            return leaf
        leaf1 = get_leaf(root1)
        leaf2 = get_leaf(root2)
        print(leaf1, leaf2)
        return leaf1 == leaf2
        