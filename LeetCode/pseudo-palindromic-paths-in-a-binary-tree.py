# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        """
        문제풀이의 주요 생각 자체는 맞췄다.
        펠린드롬 수를 확인 할 수 있는 방법은, 해당 숫자의 갯수가 홀수개인 수가 1이하인 경우(길이가 홀수면 1, 짝수면 0)이다.
        이걸 확인하는 방법은, dic에 해당 숫자를 key, 등장횟수를 value로 넣어서 value를 확인하면 된다.
        
        여기서 헷갈렸던 부분이 로직의 순서이다.
        일단, leaf노드에서만 펠린드롬 검사를 한다.
        
        그렇기때문에, 여태 풀었던 dfs문제와 다르게 일단 root.val을 추가하고
        해당 노드가 리프노드면, 펠린드롬 검사를 하고
        아니면, 해당 child로 재귀를 한다음, 맨 마지막에 dic[root.val]-=1을 한다.
        왜냐하면 if root is None으로 return되면서 끝까지 탐색한 root.val부터 pop해야 해서 그렇다.
        """
        self. answer = 0
        
        
        def dfs(root,dic):
            if root is None:
                return
            
            dic[root.val]+=1
            
            if root.left is None and root.right is None:
                count = 0
                for key,value in dic.items():
                    if value %2 != 0 :
                        count+=1
                if count<=1:
                    self.answer+=1
            
            if root.left is not None:
                dfs(root.left,dic)
                
            
            if root.right is not None:
                dfs(root.right,dic)
            
            dic[root.val]-=1
            
                
        
        if root.left is None and root.right is None:
            return 1
        else:
            dfs(root,defaultdict(int))
        return self.answer
