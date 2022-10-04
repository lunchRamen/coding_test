# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    root - leaf까지의 합이 target과 같은게 있는지 찾는거.
    끝까지 탐색해야하기때문에, dfs를 쓰는게 좋겠다.

    중간에 target과 같은건 상관없다. leaf에서 합이 target과 같아야한다. -> 조건문 삽입
    root.left or right이 남아있을때까지 재귀호출을 한다.
    만약 같은게 있다면 true 없다면 flase를 return한다.
    """
    flag = False
    def dfs(self,root,targetSum,sum_):
        sum_+=root.val
        if root.left is None and root.right is None:
            if targetSum == sum_:
                self.flag=True

        if not root:
            return
        
        if root.left is not None:
            self.dfs(root.left,targetSum,sum_)

        if root.right is not None:
            self.dfs(root.right,targetSum,sum_)
    

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        self.dfs(root,targetSum,0)

        return self.flag
