from collections import deque
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        self.answer=[]
        
        """
        첫째 자리수 (1~9)까지를 bfs돌린다.
        q의 filter는 숫자의길이가 >n이면 넘어간다.
                            ==n이면 내가 원하는 조건의 숫자길이가 나온것이므로, 저장하고 넘어간다
        만약 숫자의 마지막값 - k>=0이면,
        마지막값-k한걸 맨뒤에 더해줘서, q에 추가
        
        마지막값+k<10이면,
        마지막값+k한걸 맨뒤에 더해줘서, q에 추가.
        
        헷갈렸던 부분은, q.popleft()시켰던 number가 첫번째 조건문을 지나면 변형되어
        두번째 if문에 걸리지 않는다는 것이였다.
        """
        
        def bfs(num):
            q=deque([num])
            
            while q:
                number=str(q.popleft())
                tempNum=number
                if len(number)>n:
                    continue
                    
                if len(number)==n:
                    self.answer.append(int(number))
                    continue
                
                if int(number[-1])-k>=0:
                    temp=int(tempNum[-1])-k
                    tempNum+=str(temp)
                    q.append(int(tempNum))
                
                if int(number[-1])+k<10:
                    temp2=int(number[-1])+k
                    number+=str(temp2)
                    q.append(int(number))
                    
                
            
        
        for i in range(1,10):
            bfs(i)
        
        return set(self.answer)
