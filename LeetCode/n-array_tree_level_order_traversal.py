"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import defaultdict
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        dic=defaultdict(list)
        
        def dfs(root,depth):
            if root is None:
                return
            
            dic[depth].append(root.val)
            
            if root.children is not None:
                for i in root.children:
                    dfs(i,depth+1)
                
        dfs(root,0)
        
        answer=[]
        
        for key,value in dic.items():
            answer.append(dic[key])
        return answer
