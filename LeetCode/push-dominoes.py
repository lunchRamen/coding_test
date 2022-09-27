class Solution:
    def pushDominoes(self, d: str) -> str:
        """
        딕셔너리를 쓸라고 했는데, 안됐다.
        다른 풀이방법을 참고한다.
        
        l배열, r배열을 만든다.
        각 배열은 l또는 r을 만났을때 1부터 시작하여, 1씩 증가하다가 r또는l을 만나면 다시 0으로 초기화된다.
        이렇게 하는 이유는, 이 l과 r배열의 대소관계로, L,.,R을 정할것이기때문.
        이렇게 각 도미노마다 R은 몇, L은 몇인지 구했으면 돌면서 각 칸의 쓰러지는 방향을 정한다.
        
        각 칸을 구하는 로직은
        r>0 and l==0이면 해당칸은 R
        l>0 and r==0이면 해당칸은 L
        r==l이면 해당칸은 .
        여기서 특이한데,
        r>l이면 해당칸은 L
        r<l이면 해당칸은 R이다
        상식적으로 생각하면 수가 더 클수록, 해당 방향으로 되어야하지 않나?하지만
        도미노 구하는 로직을 살펴보면,
        *숫자가 작을수록* 더 오랜시간 도미노가 쓰러져왔다는것을 알 수 있다.
        그러므로, 숫자가 작아야 해당방향으로 쓰러지는 도미노인것.
        여기서 두 개만 비교해주면 되는 이유는 앞선 if문이 r>0 and l==0 l>0 and r==0으로 두개 다 0 이상인 경우에 한정했기때문.
        
        -> 이렇게되면 3*N시간복잡도로 해결할 수 있다.
        """
        
        n=len(d)
        r=[0 for _ in range(n)]
        l=[0 for _ in range(n)]
        result=[""]*n
        
        if d[0]=='R':
            r[0]=1
        if d[-1]=='L':
            l[-1]=1
        
        for i in range(1,n):
            if d[i]=='R':
                r[i]=1
            elif d[i]=='L':
                continue
            elif r[i-1]>0:
                r[i]=r[i-1]+1
        
        for i in range(n-2,-1,-1):
            if d[i]=='L':
                l[i]=1
            elif d[i]=='R':
                continue
            elif l[i+1]>0:
                l[i]=l[i+1]+1
        
        for i in range(n):
            if r[i] > 0 and l[i] == 0:
                result[i] = 'R'
            elif r[i] == 0 and l[i] > 0:
                result[i] = 'L'
            elif r[i] == l[i]:
                result[i] = '.'
            elif r[i] < l[i]:
                result[i] = 'R'
            elif r[i] > l[i]:
                result[i] = 'L'
        
        return "".join(result)
