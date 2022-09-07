# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    """
    node가 비었으면, 빈 문자열
    left랑 right가 둘 다 비어있으면 -> node.val만.
    right만 비어있으면 -> root + (left)를
    
    그 다음, root.val + ( left ) + (right)를 돌리면 됨.
    
    이 문제는 subtree로 node가 None이 될때까지 재귀호출하고,
    그렇게 쌓인 문자열들을 root.val + ( root.left ) + ( root.right )로 더해서 return하는 문제.
    
    여기서 포인트는, left가 비어있다면, 비어있는 ()라도 return해줘야하기때문에, (dfs)로 재귀를 태운다는 점.
    """
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        if not root.left and not root.right:
            return str(root.val)
        if not root.right:
            return str(root.val) + '(' + self.tree2str(root.left) + ')'
        
        return str(root.val) + '(' + self.tree2str(root.left) + ')(' + self.tree2str(root.right) + ')'
