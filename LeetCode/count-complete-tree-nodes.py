# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
완전 이진 트리
-> 값이 왼쪽 노드부터 순서대로 차는 트리이다.
고로, 왼쪽 subtree부터 오른쪽 subtree까지 재귀하면서, 노드 방문마다 노드 갯수를 1씩 올려서 재귀 다 호출되면 해당 노드갯수를 return 해주면 된다.
"""
class Solution:
    count_nodes = 0
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        self.count_nodes+=1

        if root.left is not None:
            self.countNodes(root.left)
        if root.right is not None:
            self.countNodes(root.right)
        
        return self.count_nodes
