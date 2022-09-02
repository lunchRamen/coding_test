from collections import defaultdict
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        """
        나는, depth를 dfs에 인자로 넘겨서, 각 인자에 맞게끔 배열을 잘라서 구현을 했었는데, 그러기보다
        dict 자체를 setdefaultdict(list)로 두고, dic의 key를 depth로 두면 코드도 훨씬 간단해지고,
        속도도 빨라진다.
        """
        
        self.dic=defaultdict(list)
        
        def dfs(root,depth):
            if root is None:
                return
            
            self.dic[depth].append(root.val)
            
            if root.left is not None:
                dfs(root.left,depth+1)
            if root.right is not None:
                dfs(root.right,depth+1)
            
        dfs(root,0)
        answer=[]
#         self.answer.sort(key=lambda x:x[1])
        
#         answerArr=[float('{:.5f}'.format(self.answer[0][0]))]
#         i=1
#         prevI=1
        
#         if len(self.answer)==1:
#             return answerArr
        
#         while i!=len(self.answer)-1:
#             if self.answer[i][1] != self.answer[i+1][1]:
#                 temp=self.answer[prevI:i+1]
#                 sumNum=0
#                 for j in range(len(temp)):
#                     sumNum+=temp[j][0]
#                 answerArr.append(float('{:.5f}'.format(sumNum/len(temp))))
#                 prevI=i+1
#             i+=1
            
#         sumNum=0
#         for j in range(prevI,len(self.answer)):
#             sumNum+=self.answer[j][0]
#         answerArr.append(float('{:.5f}'.format(sumNum/len(self.answer[prevI:]))))

        for i in self.dic:
            answer.append(round(sum(self.dic[i])/len(self.dic[i]),5))
            
        return answer
