# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        subtree를 재귀호출하는 문제
        일단, left node까지 가서, 해당 노드에 값이 없으면 -> None return
             right node까지 가서, 해당 노드에 값이 없으면 -> None return
        
        만약 자신 포함, 자식포함 subtree에 1이 하나라도 있으면, 해당 subtree return
        아니면, None return -> 이게 자신이 0이면서, 자식도 다 0이거나 자식이 다 None인 경우 해당 노드도 None처리를 해준다.
        """
        if not root:
            return None
        
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        
        if root.left or root.right or root.val == 1:
            return root
        else:
            return None
