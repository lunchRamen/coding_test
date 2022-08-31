
class Solution:
    
                
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        각 cell들을 brute force 돌려서, 상하좌우 모두 해당 셀보다 작으면, result에 append한다.
        각 cell들을 돌면서, 상 하 좌 우 극단에 닿는지 조사를 했었는데, 발상의 전환으로
        각 극단의 cell들을 dfs돌려서, 해당 원소가 pacific인지, atlantic인지를 구별하는 방법으로 가는게 더 나을듯.
        
        dfs의 통과조건
        1. heights 범위 내에 있는지
        2. 이미 arr1 or arr2에 있는지
        3. 이전 값이 더 큰지.
        없다면 dfs돌림.
        
        또한, in의 시간복잡도를 줄이기 위해 set을 사용했다.
        """
        arr1=set() #pacific = 상 좌
        arr2=set() #atlantic = 우 하
        result=[]
        
        def dfs(x,y,arr):
            
            arr.add((x,y))
            
            for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
                nx=x+dx
                ny=y+dy
                
                if 0>nx or nx>=len(heights) or 0>ny or ny>=len(heights[0]):
                    continue
                    
                if (nx,ny) in arr:
                    continue
                
                if heights[x][y]>heights[nx][ny]:
                    continue
                
                
                
                dfs(nx,ny,arr)
                
            
        
        for i in range(len(heights)):
            dfs(i,0,arr1)
            dfs(i,len(heights[0])-1,arr2)
        
        for i in range(len(heights[0])):
            dfs(0,i,arr1)
            dfs(len(heights)-1,i,arr2)
            

        
        for i in range(len(heights)):
            for j in range(len(heights[i])):
                if ((i,j) in arr1) and ((i,j) in arr2):
                    result.append([i,j])
        
#         result=[]
#         visit=[[False]*heights[0] for _ in range(len(heights))]
        
#         def dfs(x,y,prevX,prevY,heights,result,visit):
#             if prevX==0 or prevY==0 or prevX==len(heights)-1 or prevY==len(heights[0])-1:
#                 result.append([x,y])
#                 return
            
#             dx=[1,-1,0,0]
#             dy=[0,0,-1,1]
            
#             for i in range(4):
#                 nx=x+dx[i]
#                 ny=y+dy[i]
#                 if heights[prevX][prevY]>=heights[nx][ny]:
#                     if visit[nx][ny]==False:
#                         visit[nx][ny]=True
#                         dfs(x,y,nx,ny,heights,result)
#                 else:
#                     return
        
        
#         for x in range(len(heights)):
#             for y in range(len(heights[x])):
#                 visit[x][y]=True
#                 dfs(x,y,x,y,heights,result,visit)
        
        
                
                            
        return result
