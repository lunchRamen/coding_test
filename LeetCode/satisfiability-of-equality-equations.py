class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        """
        유니온 파인드 문제.
        disjoint-set = 해당 노드와 연결된 노드들이 몇개까지 있는지 union하고, 해당 set과 연결되어있는지 찾는 문제.
        
        1. 동일한 값을 가지고 있는 그룹을 만든다(union) -> ==을 가지고 있는 두 변수를 같은 그룹에 넣는다.
        2. 동일하지 않은 값을 가지고 있는 두 변수가, 같은 그룹이 아닌지 확인한다(find) -> !=를 가지고 있는 두 변수가 다른 그룹인지 확인한다.
        3. 3번을 돌다가 만약 !=인데 같은 그룹이라면, False를 다 통과했다면 True를 return한다.
        
        여기선, 알파벳 소문자들로만 이루어져있기에 union작업 진행 시, 0~25를 각 알파벳으로 하고
        각 index의 값이 같다면 같은 그룹이고, 아니라면 다른 그룹으로 생각한다.
        
        각각의 소문자에 대해서, find로 만약 초기화 안되어있다면 본인 스스로를, 연결되어있다면 연결된 그룹을 찾아서 return해준다.
        그리고, 두번째 문자를 첫번째 문자와 연결한다.
        이 과정에서, 이미 연결된 경우, find의 while문을 통해 연결의 시작점인 부모노드까지 방문하고, 부모노드를 return하게 된다.
        
        그래서 b!=c의 경우
        b와 연결된건 a, a와 연결된건 c라서 2를 return하는데, 그게 root[c]와 같기때문에 false가 나오게됨.
        이게 만약 a==c가 아닌 c==a였어도, node를 타고가서 부모노드까지 가는건 똑같기때문에 false를 뱉는다.
        """
        def find(n):    #root[n]에 뭐가 들었는지 = n이 뭐랑 연결됐는지 확인하여 return해준다. 연결된적 없는거라면 바로 n을 return하고, 연결됐다면 시작노드를 return함.
            n = ord(n) - ord('a')   #원래 root[n]에 들어갔어야 할 값을 구함.
            while root[n] != n: #해당 그룹의 시작노드까지 갈 수 있게하는 while문
                n = root[n]
            return n
        
        def union(n1, n2):
            r1, r2 = find(n1), find(n2) #각 원소의 시작노드를 찾아줌.
            root[r2] = r1   #연결된걸 표시해줌.
            
        root = list(range(26))
        
        
        for e in equations:
            if e[1] == '=':
                union(e[0], e[-1])

        for e in equations:
            if e[1] == '!' and find(e[0]) == find(e[-1]):
                # print(root,e[0],e[-1])
                # print(find(e[0]),find(e[-1]))
                return False
            
        return True
