class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        first=[]
        second=[]
        
        for i in range(len(mat[0])-1,-1,-1):
            temp=[]
            x=0
            y=i
            
            while True:
                if x==len(mat) or y==len(mat[0]):
                    break
                temp.append(mat[x][y])
                x+=1
                y+=1
            temp.sort()
            first.append(temp)
        
        
        for i in range(1,len(mat)):
            temp=[]
            x=i
            y=0
            
            while True:
                if x==len(mat) or y==len(mat[0]):
                    break
                temp.append(mat[x][y])
                x+=1
                y+=1
            temp.sort()
            second.append(temp)
        
        for i in range(len(mat[0])-1,-1,-1):
            temp=first.pop(0)
            idx=0
            x=0
            y=i
            
            while True:
                if x==len(mat) or y==len(mat[0]):
                    break
                mat[x][y]=temp[idx]
                x+=1
                y+=1
                idx+=1
                
        for i in range(1,len(mat)):
            temp=second.pop(0)
            x=i
            y=0
            idx=0
            
            while True:
                if x==len(mat) or y==len(mat[0]):
                    break
                mat[x][y]=temp[idx]
                x+=1
                y+=1
                idx+=1
            
        
        return mat
