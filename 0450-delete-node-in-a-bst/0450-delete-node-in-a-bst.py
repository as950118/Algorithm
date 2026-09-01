# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        prv = None
        cur = root

        # 삭제할 노드 탐색
        while cur and cur.val != key:
            prv = cur

            if key < cur.val:
                cur = cur.left
            else:
                cur = cur.right

        # 없는 경우
        if cur is None:
            return root

        # 1. 자식이 없는 경우
        if cur.left is None and cur.right is None:
            if prv is None:
                return None

            if prv.left == cur:
                prv.left = None
            else:
                prv.right = None

        # 2. 자식이 하나인 경우
        elif cur.left is None or cur.right is None:
            child = cur.left if cur.left else cur.right

            if prv is None:
                return child

            if prv.left == cur:
                prv.left = child
            else:
                prv.right = child

        # 3. 자식이 두 개인 경우
        else:
            # 오른쪽 서브트리의 최소값
            successor_parent = cur
            successor = cur.right

            while successor.left:
                successor_parent = successor
                successor = successor.left

            # 값 교체
            cur.val = successor.val

            # successor 삭제
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

        return root