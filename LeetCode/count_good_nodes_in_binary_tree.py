# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.answer=0
        """
        주어진 TreeNode를 배열로 만들고, 그걸 다시 역탐색하는걸 짜려고 했는데,
        주어진 자료구조 그 자체를 이해하는 법을 알아야한다.
        goodNode란 자식노드의 값 >= 부모노드가 되는 모든 경우의수를 체크하는 것.
        재귀로 호출하게되면, 호출될때마다 해당 노드 전까지 maxValue를 각각 가지고 있으므로
        현재 넘겨받은 root.val이 value보다 큰지만 알면 경우의수에 해당 됨.
        그리고, left,right에 맞게끔 재귀호출해줌.
        """
        
        def bst(root,value):
            if root==None:
                return
            
            if root.val>=value:
                self.answer+=1
                value=root.val
            
            if root.left:
                bst(root.left,value)
            if root.right:
                bst(root.right,value)
        
        
        bst(root,-10**4)
        return self.answer
