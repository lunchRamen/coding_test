# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        """
        depth-1부분에 노드를 삽입한다
        -> depth-2를 부모로, depth-1를 자식으로 삼는 노드를 끼워넣어야함.
        또한, left는 left의 subtree의 parent로 right는 right의 subtree의 parent로 만들어야함
        그래서 node를 2개 만들고, 자식으로 붙일 노드는 deepcopy하여 참조값이 아닌 객체값 그 자체를 가져온다
        그 다음, root.left와 root.right를 갱신.
        그 다음 root.left.left와 root.right.right로 원래 있던 left right subtree를 잇는다.
        """
        def dfs(root,val,depth,idx,dist):
            if depth-2 == idx:
                t1 = TreeNode(val)
                t2 = TreeNode(val)

                temp1 = copy.deepcopy(root.left)
                temp2 = copy.deepcopy(root.right)

                root.left = t1
                root.right = t2

                root.left.left = temp1
                root.right.right = temp2
                return
                    
            if not root:
                return

            if root.left:
                dfs(root.left,val,depth,idx+1,-1)
            if root.right:
                dfs(root.right,val,depth,idx+1,1)
        
        if depth == 1:
            temp = copy.deepcopy(root)
            t = TreeNode(val)
            t.left = temp
            return t

        dfs(root,val,depth,0,0)
        return root
