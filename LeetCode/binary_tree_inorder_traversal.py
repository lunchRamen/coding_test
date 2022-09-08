# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        전위 순회 = left sub -> root -> right sub
        중위 순회 = root -> left sub -> right sub
        후위 순회 = left sub -> right sub -> root
        
        이중 전위순회 구현.
        전위순회의 경우, 모든 left subtree가 출력 되고, root가 출력되어야함.
        그래서 list에 추가하는 로직이 left subtree recursion이 다 호출된 후에 해야하는 것.
        
        코드의 흐름을 보자면,
        left sub의 left node의 자식노드(=None)이 나올때까지,
        if root.left is not None: dfs(root.left); 가 실행된다.
        그 후, if root is None:에 걸려서 return되면, (사실 이게 없어도 정상동작한다. 재귀를 태우는거 자체가 자식노드에 값이 있어야 돌아가서.)
        그 후에 해당 재귀함수에서 걸리는 코드는 self.answer.append(root.val)이다
        그래서 [1,2,3,4,5,6,7,8]의 예제의 경우
        8의 자식노드까지 가서 return되고, 8이 추가되고
        if root.right is not None을 해보지만 오른쪽 자식이 없어서 해당 재귀함수는 끝남
        그러면, 4로 올라가서 4를 추가하고, 똑같이 오른쪽 자식이 없어서 끝남
        그 다음, 2로 올라가서 2를 추가하고, 오른쪽 자식 5를 추가하고 끝남.
        여기서 오른쪽 자식 5가 추가되는 이유는, 5의 재귀함수가 호출이 되면
        if root is None -> 5라서 pass
        if root.left is not None -> 왼쪽자식 없어서 pass
        5추가
        if root.right is not None -> 오른쪽 자식 없어서 pass 여서 5가 추가됨.
        이후 5의 함수가끝나고 1의 함수 호출
        그다음 1의 right sub인 3 6 7이 호출되는데, 위와 똑같은 방식으로 호출 된다.
        """
        self.answer=[]
        def dfs(root):
            print(self.answer)
            if root is None:
                return
            
            if root.left is not None:
                dfs(root.left)
            
            self.answer.append(root.val)
            
            if root.right is not None:
                dfs(root.right)
        
        dfs(root)
        return self.answer
