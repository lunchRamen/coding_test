# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        """
        해당 문제는, 이분트리를 좌표평면상으로 row,col과 해당 node.val까지 따지는 문제.
        먼저, col순으로 정렬을 한 후, 해당 col순으로 answer에 root.val을 추가한다.
        col은 음수도 포함되므로, list의 idx체계에 맞지 않아 defaultdict(list)를 사용.
        그리고, 우리는 row, node.val 모두 필요하기때문에 해당 값을 list형태로 dic[col]에 저장한다.
        
        그 후, dic의 key값으로 정렬한 리스트를 만든다.
        그 다음 해당 list를 돌면서 정답에 넣을 root.val을 추가하는데,
        해당 root.val의 추가 조건은
        1. row(=depth)가 낮은 순서
        2. row가 같다면, node.val이 낮은 순서대로 정렬을 한 후, 값을 추가한다.
        그러므로, 내가 저장한 [row,root.val]의 순서에서
        파이썬의 sort(key= lambda x:)를 이용해 (x[0],x[1])로
        row순 오름차순으로 먼저 정렬 후, 같다면 node.val의 오름차순으로 정렬한 temp2를 만든다.
        그 후 temp2의 temp2[1]값들을 차례대로 정답에 추가하면 끝.
        """
        dic=defaultdict(list)
        answer=[]
        
        def dfs(root,row,col):
            if root is None:
                return
            dic[col].append([row,root.val])
            
            if root.left is not None:
                dfs(root.left, row+1,col-1)
                
            if root.right is not None:
                dfs(root.right,row+1,col+1)
            
        dfs(root,0,0)
        answerList=sorted(dic.items())
        
        for item in answerList:
            temp=[]
            for i in item[1]:
                temp.append(i)
            #row가 낮은순 다음 값이 작은순
            temp.sort(key=lambda x: (x[0],x[1]))
            temp2=[]
            for idx in temp:
                temp2.append(idx[1])
            answer.append(temp2)
        return answer
